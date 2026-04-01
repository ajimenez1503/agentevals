"""Utilities for parsing OTel GenAI semantic convention message formats.

Supports two message formats:
- Content-based (e.g. opentelemetry-instrumentation-openai-v2):
    {"role": "user", "content": "Hello"}
    {"role": "assistant", "content": "...", "tool_calls": [{"type": "function", ...}]}

- Parts-based (OTel GenAI semconv v1.36.0+):
    {"role": "user", "parts": [{"type": "text", "content": "Hello"}]}
    {"role": "assistant", "parts": [{"type": "tool_call", "name": "...", "arguments": {...}}]}
"""

from __future__ import annotations

import json
import logging
from typing import Any

from ..trace_attrs import (
    OTEL_GENAI_INPUT_MESSAGES,
    OTEL_GENAI_LEGACY_COMPLETION_PREFIX,
    OTEL_GENAI_LEGACY_PROMPT_PREFIX,
    OTEL_GENAI_OUTPUT_MESSAGES,
)

logger = logging.getLogger(__name__)

USER_ROLES = ("user", "human")
ASSISTANT_ROLES = ("assistant", "model", "ai")


def parse_json_attr(raw: str | dict | list | Any, tag_name: str = "") -> dict | list | Any:
    """Parse a JSON string from an OTel span attribute value.

    If *raw* is already a dict or list it is returned as-is.
    Returns ``{}`` on parse failure.
    """
    if isinstance(raw, (dict, list)):
        return raw
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            logger.warning("Failed to parse JSON in %s: %s", tag_name, raw[:200])
            return {}
    return {}


def _get_messages_from_attrs(
    attrs: dict[str, Any],
    key: str,
    legacy_prefix: str,
) -> list[dict]:
    """Read GenAI messages from modern JSON attr or legacy indexed attrs.

    Modern format:
      - gen_ai.input.messages / gen_ai.output.messages as JSON arrays

    Legacy format:
      - gen_ai.prompt.<idx>.<field>
      - gen_ai.completion.<idx>.<field>
    """
    modern_raw = attrs.get(key)
    if modern_raw is not None:
        parsed = parse_json_attr(modern_raw, key)
        if isinstance(parsed, list) and parsed:
            return [m for m in parsed if isinstance(m, dict)]

    return _parse_legacy_indexed_messages(attrs, legacy_prefix)


def get_input_messages_from_attrs(attrs: dict[str, Any]) -> list[dict]:
    return _get_messages_from_attrs(
        attrs,
        OTEL_GENAI_INPUT_MESSAGES,
        OTEL_GENAI_LEGACY_PROMPT_PREFIX,
    )


def get_output_messages_from_attrs(attrs: dict[str, Any]) -> list[dict]:
    return _get_messages_from_attrs(
        attrs,
        OTEL_GENAI_OUTPUT_MESSAGES,
        OTEL_GENAI_LEGACY_COMPLETION_PREFIX,
    )


def extract_text_from_message(msg: dict) -> str:
    """Extract text content from a GenAI message in any supported format."""
    content = msg.get("content")
    if isinstance(content, str) and content:
        return content
    if isinstance(content, list):
        parts = [item["text"] for item in content if isinstance(item, dict) and "text" in item]
        if parts:
            return " ".join(parts)

    parts = msg.get("parts")
    if isinstance(parts, list):
        text_parts = []
        for part in parts:
            if not isinstance(part, dict) or part.get("type") != "text":
                continue
            text = part.get("content") or part.get("text", "")
            if text:
                text_parts.append(text)
        if text_parts:
            return " ".join(text_parts)

    return ""


def extract_tool_calls_from_message(msg: dict) -> list[dict[str, Any]]:
    """Extract tool calls from a GenAI message in any supported format.

    Returns a normalized list of:
        {"name": str, "id": str | None, "arguments": dict}
    """
    result = []

    tool_calls = msg.get("tool_calls")
    if isinstance(tool_calls, list):
        for tc in tool_calls:
            if not isinstance(tc, dict):
                continue
            if tc.get("type") == "function" and "function" in tc:
                func = tc["function"]
                args = _parse_args(func.get("arguments", {}))
                result.append(
                    {
                        "name": func.get("name", ""),
                        "id": tc.get("id"),
                        "arguments": args,
                    }
                )
            elif tc.get("name"):
                # Legacy flattened format commonly emits:
                # tool_calls.<idx>.name / tool_calls.<idx>.arguments
                args = _parse_args(tc.get("arguments", {}))
                result.append(
                    {
                        "name": tc.get("name", ""),
                        "id": tc.get("id"),
                        "arguments": args,
                    }
                )

    if not result:
        parts = msg.get("parts")
        if isinstance(parts, list):
            for part in parts:
                if not isinstance(part, dict) or part.get("type") != "tool_call":
                    continue
                args = _parse_args(part.get("arguments", {}))
                result.append(
                    {
                        "name": part.get("name", ""),
                        "id": part.get("id"),
                        "arguments": args,
                    }
                )

    return result


def extract_tool_call_args_from_messages(
    messages_raw: str | list | Any,
    tool_name: str,
) -> tuple[dict, str | None]:
    """Fallback: extract tool call args and ID from a messages attribute by matching *tool_name*.

    Used when a tool span lacks ``gen_ai.tool.call.arguments`` directly
    (e.g. Strands embeds the triggering tool_call in ``gen_ai.input.messages``).

    Returns ``(args_dict, tool_call_id_or_None)``.
    """
    messages = parse_json_attr(messages_raw, "gen_ai.input.messages")
    if not isinstance(messages, list):
        return {}, None
    for msg in messages:
        if not isinstance(msg, dict):
            continue
        for tc in extract_tool_calls_from_message(msg):
            if tc["name"] == tool_name and tc["arguments"]:
                return tc["arguments"], tc.get("id")
    return {}, None


def _parse_args(args: Any) -> dict:
    if isinstance(args, dict):
        return args
    if isinstance(args, str):
        try:
            parsed = json.loads(args)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            logger.warning("Failed to parse tool call arguments JSON: %s", args[:200])
    return {}


def _parse_legacy_indexed_messages(attrs: dict[str, Any], prefix: str) -> list[dict]:
    """Reconstruct legacy GenAI messages from flattened indexed attributes."""
    by_index: dict[int, dict] = {}
    key_prefix = f"{prefix}."

    for key, value in attrs.items():
        if not isinstance(key, str) or not key.startswith(key_prefix):
            continue

        suffix = key[len(key_prefix) :]
        first, sep, rest = suffix.partition(".")
        if not sep or not first.isdigit():
            continue

        msg_idx = int(first)
        msg = by_index.setdefault(msg_idx, {})
        _set_nested_value(msg, rest.split("."), value)

    return [by_index[i] for i in sorted(by_index.keys()) if by_index[i]]


def _set_nested_value(container: dict[str, Any] | list[Any], path_parts: list[str], value: Any) -> None:
    current: dict[str, Any] | list[Any] = container

    for i, part in enumerate(path_parts):
        is_last = i == len(path_parts) - 1
        next_is_index = i + 1 < len(path_parts) and path_parts[i + 1].isdigit()

        if part.isdigit():
            if not isinstance(current, list):
                return
            idx = int(part)
            while len(current) <= idx:
                current.append([] if next_is_index else {})
            if is_last:
                current[idx] = value
                return
            expected = list if next_is_index else dict
            if not isinstance(current[idx], expected):
                current[idx] = [] if next_is_index else {}
            current = current[idx]
        else:
            if not isinstance(current, dict):
                return
            if is_last:
                current[part] = value
                return
            expected = list if next_is_index else dict
            if not isinstance(current.get(part), expected):
                current[part] = [] if next_is_index else {}
            current = current[part]
