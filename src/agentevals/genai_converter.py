"""Convert trace spans using GenAI semantic conventions into ADK Invocation objects.

Supports traces from frameworks using OpenTelemetry GenAI semantic conventions:
- LangChain (via LANGSMITH_OTEL_ENABLED)
- Any framework using standard gen_ai.* attributes
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field

from google.adk.evaluation.eval_case import IntermediateData, Invocation
from google.genai import types as genai_types

from .converter import ConversionResult
from .extraction import GenAIExtractor, is_invocation_span, is_llm_span, parse_tool_response_content
from .loader.base import Span, Trace
from .trace_attrs import (
    OTEL_GENAI_LEGACY_COMPLETION_PREFIX,
    OTEL_GENAI_TOOL_CALL_ARGUMENTS,
    OTEL_GENAI_TOOL_CALL_ID,
    OTEL_GENAI_TOOL_CALL_RESULT,
    OTEL_GENAI_TOOL_NAME,
)
from .utils.genai_messages import (
    ASSISTANT_ROLES,
    USER_ROLES,
    extract_text_from_message,
    extract_tool_call_args_from_messages,
    extract_tool_calls_from_message,
    get_input_messages_from_attrs,
    get_output_messages_from_attrs,
    parse_json_attr,
)

logger = logging.getLogger(__name__)


@dataclass
class _ToolCall:
    name: str
    args: dict
    id: str | None = None


@dataclass
class _ToolResponse:
    name: str
    response: dict
    id: str | None = None


@dataclass
class _ConversationTurn:
    invocation_id: str
    user_text: str
    assistant_text: str
    tool_calls: list[_ToolCall] = field(default_factory=list)
    tool_responses: list[_ToolResponse] = field(default_factory=list)
    start_time: float = 0.0


def convert_genai_trace(trace: Trace) -> ConversionResult:
    result = ConversionResult(trace_id=trace.trace_id)

    logger.debug(f"Converting GenAI trace {trace.trace_id} ({len(trace.all_spans)} spans)")

    llm_root_spans = [s for s in trace.root_spans if is_llm_span(s)]

    if llm_root_spans:
        has_messages = any(
            get_input_messages_from_attrs(s.tags) or get_output_messages_from_attrs(s.tags) for s in llm_root_spans
        )
        if not has_messages:
            msg = (
                f"Trace {trace.trace_id}: GenAI LLM spans found but missing message content. "
                "This usually means logs were not enriched into spans. "
                "Conversion may fail or produce incomplete results."
            )
            logger.warning(msg)
            result.warnings.append(msg)

    if len(llm_root_spans) > 1:
        if not any(is_invocation_span(s) for s in llm_root_spans):
            has_enriched = any(
                get_input_messages_from_attrs(s.tags) and get_output_messages_from_attrs(s.tags)
                for s in llm_root_spans
            )

            if has_enriched and _is_broadcast_enriched(llm_root_spans[0]):
                logger.debug(f"Multi-turn conversation: {len(llm_root_spans)} LLM spans")
                try:
                    turns = _extract_multiturn_turns(llm_root_spans)
                    for turn in turns:
                        result.invocations.append(_turn_to_invocation(turn))
                except Exception as exc:
                    msg = f"Trace {trace.trace_id}: failed to convert multi-turn conversation: {exc}"
                    logger.warning(msg)
                    result.warnings.append(msg)
                return result

    invocation_spans = _find_genai_invocation_spans(trace)
    logger.debug(f"Found {len(invocation_spans)} invocation spans")

    if not invocation_spans:
        result.warnings.append(f"Trace {trace.trace_id}: no GenAI invocation spans found")
        return result

    turns: list[_ConversationTurn] = []
    for inv_span in invocation_spans:
        try:
            turn = _extract_single_turn(inv_span)
            turns.append(turn)
        except Exception as exc:
            msg = f"Failed to convert span {inv_span.span_id}: {exc}"
            logger.warning(msg)
            result.warnings.append(msg)

    turns = _trim_cumulative_tool_trajectory(turns)
    for turn in turns:
        result.invocations.append(_turn_to_invocation(turn))

    result.invocations = _deduplicate_invocations(result.invocations)
    return result


def _find_genai_invocation_spans(trace: Trace) -> list[Span]:
    candidates = []

    for span in trace.root_spans:
        if is_invocation_span(span):
            candidates.append(span)

    if not candidates:
        for span in trace.root_spans:
            if _has_llm_children(span):
                candidates.append(span)

    if not candidates and trace.root_spans:
        llm_spans = [s for s in trace.root_spans if is_llm_span(s)]

        if len(llm_spans) > 1:
            has_enriched_messages = any(
                get_input_messages_from_attrs(s.tags) or get_output_messages_from_attrs(s.tags)
                for s in llm_spans
            )

            if has_enriched_messages and _is_broadcast_enriched(llm_spans[0]):
                logger.debug(
                    f"Found {len(llm_spans)} LLM spans with broadcast-enriched messages, treating as single multi-turn conversation"
                )
                return [llm_spans[0]]

        logger.debug("No clear invocation spans found, treating each root span as invocation")
        candidates = llm_spans if llm_spans else trace.root_spans

    if not candidates and trace.root_spans:
        logger.debug("Falling back to all root spans")
        candidates = list(trace.root_spans)

    candidates.sort(key=lambda s: s.start_time)
    return candidates


def _extract_single_turn(inv_span: Span) -> _ConversationTurn:
    llm_spans = _find_llm_spans(inv_span)

    logger.debug(f"Converting invocation span: {inv_span.operation_name}")
    logger.debug(f"Found {len(llm_spans)} LLM spans")

    if not llm_spans:
        if is_llm_span(inv_span):
            llm_spans = [inv_span]
        else:
            raise ValueError(f"Invocation span {inv_span.span_id} has no LLM call spans")

    tool_spans = _find_tool_spans(inv_span)
    logger.debug(f"Found {len(tool_spans)} tool spans")

    user_text = _extract_user_text(llm_spans[0])
    assistant_text = _extract_assistant_text(llm_spans[-1])
    tool_calls, tool_responses = _extract_tool_calls(tool_spans, llm_spans)

    return _ConversationTurn(
        invocation_id=f"genai-{inv_span.span_id}",
        user_text=user_text,
        assistant_text=assistant_text,
        tool_calls=tool_calls,
        tool_responses=tool_responses,
        start_time=float(inv_span.start_time),
    )


def _extract_multiturn_turns(llm_spans: list[Span]) -> list[_ConversationTurn]:
    all_input_messages = get_input_messages_from_attrs(llm_spans[0].tags)
    all_output_messages = get_output_messages_from_attrs(llm_spans[0].tags)

    if not all_input_messages or not all_output_messages:
        logger.warning("Missing input/output messages, falling back to single invocation")
        user_text = _extract_user_text(llm_spans[0])
        assistant_text = _extract_assistant_text(llm_spans[-1])
        return [
            _ConversationTurn(
                invocation_id=f"genai-{llm_spans[0].span_id}",
                user_text=user_text,
                assistant_text=assistant_text,
                start_time=float(llm_spans[0].start_time),
            )
        ]

    user_messages = [msg for msg in all_input_messages if msg.get("role") in USER_ROLES]
    assistant_messages = [msg for msg in all_output_messages if msg.get("role") in ASSISTANT_ROLES]

    logger.debug(f"Multi-turn: {len(user_messages)} user, {len(assistant_messages)} assistant messages")
    for i, msg in enumerate(assistant_messages):
        has_content = bool(msg.get("content"))
        has_tools = bool(msg.get("tool_calls"))
        logger.debug(f"  Assistant msg {i}: has_content={has_content}, has_tools={has_tools}")

    turns = []
    assistant_idx = 0

    for user_idx, user_msg in enumerate(user_messages):
        user_text = extract_text_from_message(user_msg)
        if not user_text:
            continue

        tool_calls: list[_ToolCall] = []
        assistant_text = ""

        while assistant_idx < len(assistant_messages):
            assistant_msg = assistant_messages[assistant_idx]

            for tc in extract_tool_calls_from_message(assistant_msg):
                tool_calls.append(_ToolCall(name=tc["name"], args=tc["arguments"], id=tc["id"]))

            content = extract_text_from_message(assistant_msg)
            if content:
                assistant_text = content
                assistant_idx += 1
                break

            assistant_idx += 1

        turns.append(
            _ConversationTurn(
                invocation_id=f"genai-turn-{user_idx + 1}-{llm_spans[0].span_id[:8]}",
                user_text=user_text if isinstance(user_text, str) else "",
                assistant_text=assistant_text,
                tool_calls=tool_calls,
                start_time=float(llm_spans[0].start_time),
            )
        )

    return turns


def _deduplicate_invocations(invocations: list[Invocation]) -> list[Invocation]:
    """Deduplicate invocations with the same user text, keeping the best one.

    The OpenAI instrumentor creates separate LLM calls for tool-use loops within
    a single conversation turn. Each call logs the full conversation history, so
    multiple spans produce invocations with the same user text. We keep the last
    one per unique user text — it has the final response (not the intermediate
    tool-call-only response).
    """
    if len(invocations) <= 1:
        return invocations

    def _user_text(inv: Invocation) -> str:
        if inv.user_content and inv.user_content.parts:
            return inv.user_content.parts[0].text or ""
        return ""

    seen: dict[str, int] = {}
    always_keep: set[int] = set()
    for i, inv in enumerate(invocations):
        text = _user_text(inv)
        if not text.strip():
            always_keep.add(i)
        else:
            seen[text] = i

    if len(seen) + len(always_keep) == len(invocations):
        return invocations

    keep = always_keep | set(seen.values())
    return [inv for i, inv in enumerate(invocations) if i in keep]


def _turn_to_invocation(turn: _ConversationTurn) -> Invocation:
    user_content = genai_types.Content(
        role="user",
        parts=[genai_types.Part(text=turn.user_text)],
    )
    final_response = genai_types.Content(
        role="model",
        parts=[genai_types.Part(text=turn.assistant_text)],
    )
    tool_uses = [genai_types.FunctionCall(name=tc.name, args=tc.args, id=tc.id) for tc in turn.tool_calls]
    tool_responses = [
        genai_types.FunctionResponse(name=tr.name, response=tr.response, id=tr.id) for tr in turn.tool_responses
    ]
    return Invocation(
        invocation_id=turn.invocation_id,
        user_content=user_content,
        final_response=final_response,
        intermediate_data=IntermediateData(tool_uses=tool_uses, tool_responses=tool_responses),
        creation_timestamp=turn.start_time / 1_000_000.0,
    )


def _extract_user_text(llm_span: Span) -> str:
    messages = get_input_messages_from_attrs(llm_span.tags)

    for msg in reversed(messages):
        if msg.get("role") in USER_ROLES:
            text = extract_text_from_message(msg)
            if text:
                logger.debug(f"Found user message: {text[:100]}")
                return text

    logger.warning(f"No user message found in {len(messages)} messages")
    raise ValueError(f"LLM span {llm_span.span_id}: no user message found in gen_ai.input.messages")


def _extract_assistant_text(llm_span: Span) -> str:
    messages = get_output_messages_from_attrs(llm_span.tags)

    logger.debug(f"Extracting final response from {len(messages)} output messages")
    for i, msg in enumerate(messages):
        if isinstance(msg, dict):
            logger.debug(
                f"  Message {i}: role={msg.get('role')}, content_len={len(msg.get('content', ''))}, has_tool_calls={bool(msg.get('tool_calls'))}"
            )

    for msg in reversed(messages):
        if msg.get("role") in ASSISTANT_ROLES:
            text = extract_text_from_message(msg)
            if text:
                logger.debug(f"Found assistant message with text: {text[:100]}")
                return text

    if _is_legacy_completion_without_content(llm_span):
        logger.debug(
            "LLM span %s: legacy gen_ai.completion has no content; treating as empty assistant response",
            llm_span.span_id,
        )
        return ""

    logger.warning(
        f"LLM span {llm_span.span_id}: no assistant message with content in gen_ai.output.messages ({len(messages)} messages)"
    )
    return ""


def _trim_cumulative_output(llm_span: Span, output_messages: list[dict]) -> list[dict]:
    """For cumulative-history traces, return only the current turn's output messages.

    The OpenAI instrumentor v2 stores the full conversation history in each span.
    Each span's output includes ALL previous turns' assistant responses. Given N
    user messages in input, the current turn is N. We skip past the first (N-1)
    assistant text responses in the output — everything after that belongs to the
    current turn.
    """
    input_messages = get_input_messages_from_attrs(llm_span.tags)
    if not input_messages:
        return output_messages

    user_count = sum(1 for m in input_messages if isinstance(m, dict) and m.get("role") in USER_ROLES)
    if user_count <= 1:
        return output_messages

    previous_turns = user_count - 1
    text_responses_seen = 0

    for i, msg in enumerate(output_messages):
        if not isinstance(msg, dict) or msg.get("role") not in ASSISTANT_ROLES:
            continue
        content = extract_text_from_message(msg)
        if content:
            text_responses_seen += 1
            if text_responses_seen >= previous_turns:
                trimmed = output_messages[i + 1 :]
                logger.debug(
                    "Trimmed cumulative output: %d → %d messages (skipped %d previous turns)",
                    len(output_messages),
                    len(trimmed),
                    previous_turns,
                )
                return trimmed

    return output_messages


def _extract_tool_calls(
    tool_spans: list[Span],
    llm_spans: list[Span] | None = None,
) -> tuple[list[_ToolCall], list[_ToolResponse]]:
    tool_calls_by_id: dict[str, _ToolCall] = {}
    tool_calls_no_id: list[_ToolCall] = []
    tool_responses: list[_ToolResponse] = []

    for tool_span in tool_spans:
        tool_name = tool_span.get_tag(OTEL_GENAI_TOOL_NAME)
        if not tool_name:
            logger.warning(f"Tool span missing gen_ai.tool.name: {tool_span.operation_name}")
            continue

        tool_call_id = tool_span.get_tag(OTEL_GENAI_TOOL_CALL_ID)

        args_raw = tool_span.get_tag(OTEL_GENAI_TOOL_CALL_ARGUMENTS, "{}")
        args = parse_json_attr(args_raw, "gen_ai.tool.call.arguments")
        if not isinstance(args, dict):
            args = {}

        if not args:
            input_msgs = get_input_messages_from_attrs(tool_span.tags)
            if input_msgs:
                args, _ = extract_tool_call_args_from_messages(input_msgs, tool_name)

        tc = _ToolCall(name=tool_name, args=args, id=tool_call_id)
        if tool_call_id:
            tool_calls_by_id[tool_call_id] = tc
        else:
            tool_calls_no_id.append(tc)

        result_raw = tool_span.get_tag(OTEL_GENAI_TOOL_CALL_RESULT)
        if result_raw:
            result_data = parse_tool_response_content(result_raw)
            logger.debug(f"Tool {tool_name} result: {str(result_data)[:100]}")
            tool_responses.append(
                _ToolResponse(
                    name=tool_name,
                    response=result_data,
                    id=tool_call_id,
                )
            )
        else:
            output_msgs = get_output_messages_from_attrs(tool_span.tags)
            if output_msgs:
                for msg in output_msgs:
                    if not isinstance(msg, dict):
                        continue
                    for part in msg.get("parts", []):
                        if not isinstance(part, dict):
                            continue
                        if part.get("type") == "tool_call_response" and "response" in part:
                            resp = part["response"]
                            if isinstance(resp, list):
                                texts = [t.get("text", "") for t in resp if isinstance(t, dict) and "text" in t]
                                result_data = parse_tool_response_content(" ".join(texts))
                            elif isinstance(resp, dict):
                                result_data = resp
                            else:
                                result_data = {"result": str(resp)}
                            tool_responses.append(
                                _ToolResponse(
                                    name=tool_name,
                                    response=result_data,
                                    id=tool_call_id,
                                )
                            )
                            break

    if llm_spans:
        for llm_span in llm_spans:
            messages = get_output_messages_from_attrs(llm_span.tags)
            if not messages:
                continue

            messages = _trim_cumulative_output(llm_span, messages)

            for msg in messages:
                if msg.get("role") not in ASSISTANT_ROLES:
                    continue
                for tc in extract_tool_calls_from_message(msg):
                    tc_id = tc["id"]
                    new_tc = _ToolCall(
                        name=tc["name"],
                        args=tc["arguments"],
                        id=tc_id,
                    )
                    if tc_id and tc_id in tool_calls_by_id:
                        # Prefer LLM message version if it has richer args
                        existing = tool_calls_by_id[tc_id]
                        if tc["arguments"] and not existing.args:
                            tool_calls_by_id[tc_id] = new_tc
                    elif tc_id:
                        tool_calls_by_id[tc_id] = new_tc
                    else:
                        tool_calls_no_id.append(new_tc)

    # Legacy Ollama traces can carry tool trajectory only in input history
    # (gen_ai.prompt.*), while output (gen_ai.completion.*) has role-only data.
    if llm_spans and not tool_spans and not tool_calls_by_id and not tool_calls_no_id and not tool_responses:
        legacy_calls, legacy_responses = _extract_tools_from_input_history(
            get_input_messages_from_attrs(llm_spans[-1].tags)
        )
        for call in legacy_calls:
            if call.id:
                tool_calls_by_id.setdefault(call.id, call)
            else:
                tool_calls_no_id.append(call)
        tool_responses.extend(legacy_responses)

    tool_calls = list(tool_calls_by_id.values()) + tool_calls_no_id
    logger.debug(f"Extracted {len(tool_calls)} tool calls, {len(tool_responses)} responses")
    return tool_calls, tool_responses


def _extract_tools_from_input_history(messages: list[dict]) -> tuple[list[_ToolCall], list[_ToolResponse]]:
    calls: list[_ToolCall] = []
    responses: list[_ToolResponse] = []
    pending: list[_ToolCall] = []

    for msg in messages:
        if not isinstance(msg, dict):
            continue
        role = msg.get("role")

        if role in ASSISTANT_ROLES:
            for tc in extract_tool_calls_from_message(msg):
                call = _ToolCall(name=tc["name"], args=tc["arguments"], id=tc["id"])
                calls.append(call)
                pending.append(call)
            continue

        if role == "tool":
            text = extract_text_from_message(msg)
            if not text:
                continue
            parsed = parse_tool_response_content(text)
            if pending:
                matched = pending.pop(0)
                responses.append(_ToolResponse(name=matched.name, response=parsed, id=matched.id))
            else:
                responses.append(
                    _ToolResponse(
                        name=msg.get("name", "tool"),
                        response=parsed,
                        id=msg.get("tool_call_id"),
                    )
                )

    return calls, responses


def _trim_cumulative_tool_trajectory(turns: list[_ConversationTurn]) -> list[_ConversationTurn]:
    """Trim cumulative tool trajectory across sequential turns.

    Some legacy traces repeat full prior tool history in each subsequent turn.
    If turn N's tools are a strict prefix-extension of turn N-1, keep only the
    newly introduced suffix for turn N.
    """
    prev_calls: list[_ToolCall] = []
    prev_responses: list[_ToolResponse] = []

    for turn in turns:
        original_calls = turn.tool_calls
        original_responses = turn.tool_responses

        if (
            prev_calls
            and len(original_calls) > len(prev_calls)
            and original_calls[: len(prev_calls)] == prev_calls
        ):
            turn.tool_calls = original_calls[len(prev_calls) :]

        if (
            prev_responses
            and len(original_responses) > len(prev_responses)
            and original_responses[: len(prev_responses)] == prev_responses
        ):
            turn.tool_responses = original_responses[len(prev_responses) :]

        prev_calls = original_calls
        prev_responses = original_responses

    return turns


_genai_extractor = GenAIExtractor()


def _is_broadcast_enriched(span: Span) -> bool:
    """Detect whether a span was enriched via broadcast (all messages in every span).

    Broadcast enrichment (WebSocket path) injects the full conversation history
    into every span, so the first span has multiple user messages.
    Per-span enrichment (OTLP path) gives each span only its own messages,
    so each span has at most 1 user message.
    """
    messages = get_input_messages_from_attrs(span.tags)
    if not messages:
        return False
    user_count = sum(1 for m in messages if isinstance(m, dict) and m.get("role") in USER_ROLES)
    return user_count > 1


def _find_llm_spans(root: Span) -> list[Span]:
    return _genai_extractor.find_llm_spans_in(root)


def _find_tool_spans(root: Span) -> list[Span]:
    return _genai_extractor.find_tool_spans_in(root)


def _has_llm_children(span: Span) -> bool:
    return _genai_extractor._has_llm_children(span)


def _is_legacy_completion_without_content(span: Span) -> bool:
    has_legacy_completion = False
    has_legacy_completion_content = False

    for key in span.tags:
        if not isinstance(key, str):
            continue
        if key.startswith(f"{OTEL_GENAI_LEGACY_COMPLETION_PREFIX}."):
            has_legacy_completion = True
            if key.endswith(".content"):
                has_legacy_completion_content = True

    return has_legacy_completion and not has_legacy_completion_content
