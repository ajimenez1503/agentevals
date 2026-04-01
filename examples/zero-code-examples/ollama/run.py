"""Run the LangChain dice agent against a local Ollama model with OTLP export.

Demonstrates zero-code integration with a local LLM provider:
the agent emits standard OpenTelemetry spans/logs and sends them to agentevals
via OTLP, without using the agentevals Python SDK in agent code.

This example uses Ollama's native LangChain chat client.

Prerequisites:
    1. python -m venv .venv
    2. source .venv/bin/activate
    3. pip install -r requirements.txt
    4. agentevals serve --dev
    5. ollama serve
    6. ollama pull llama3.2:3b

Optional OTLP debug collector (instead of agentevals on port 4318):
    docker run --rm -it -p 4318:4318 otel/opentelemetry-collector-contrib:latest

Usage:
    python examples/zero-code-examples/test2/run.py

Optional environment variables:
    LOCAL_OLLAMA_BASE_URL (default: http://localhost:11434)
    LOCAL_LLM_MODEL (default: llama3.2:3b)
"""

import os
import random
import json

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from opentelemetry import trace
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.ollama import OllamaInstrumentor
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

load_dotenv(override=True)


@tool
def roll_die(sides: int = 6) -> dict:
    """Roll a die with a specified number of sides."""
    if sides < 2:
        return {"sides": sides, "result": None, "message": "Error: Die must have at least 2 sides"}

    result = random.randint(1, sides)
    return {"sides": sides, "result": result, "message": f"Rolled a {result} on a {sides}-sided die"}


@tool
def check_prime(nums: list[int]) -> dict:
    """Check if numbers are prime."""

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    results = {n: is_prime(n) for n in nums}
    prime_numbers = [n for n, is_p in results.items() if is_p]

    return {"results": results, "prime_count": len(prime_numbers), "prime_numbers": prime_numbers}


def _maybe_json_parse(value):
    if not isinstance(value, str):
        return value
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def _normalize_tool_args(tool_name: str, tool_args):
    parsed = _maybe_json_parse(tool_args)

    if tool_name == "roll_die":
        if isinstance(parsed, dict):
            sides = _maybe_json_parse(parsed.get("sides"))
            if isinstance(sides, str) and sides.strip().lstrip("-").isdigit():
                parsed["sides"] = int(sides.strip())
            elif isinstance(sides, (int, float)):
                parsed["sides"] = int(sides)
            return parsed
        if isinstance(parsed, str) and parsed.strip().lstrip("-").isdigit():
            return {"sides": int(parsed.strip())}
        if isinstance(parsed, (int, float)):
            return {"sides": int(parsed)}
        return parsed

    if tool_name == "check_prime":
        if isinstance(parsed, list):
            parsed = {"nums": parsed}
        elif isinstance(parsed, (int, float)):
            parsed = {"nums": [int(parsed)]}
        elif isinstance(parsed, str):
            stripped = parsed.strip()
            if stripped.lstrip("-").isdigit():
                parsed = {"nums": [int(stripped)]}

        if isinstance(parsed, dict):
            nums = _maybe_json_parse(parsed.get("nums"))
            if isinstance(nums, (int, float)):
                nums = [int(nums)]
            elif isinstance(nums, str):
                stripped = nums.strip()
                if stripped.lstrip("-").isdigit():
                    nums = [int(stripped)]
                else:
                    parts = [p.strip() for p in stripped.split(",") if p.strip()]
                    if parts and all(p.lstrip("-").isdigit() for p in parts):
                        nums = [int(p) for p in parts]
            elif isinstance(nums, list):
                normalized = []
                for n in nums:
                    n = _maybe_json_parse(n)
                    if isinstance(n, (int, float)):
                        normalized.append(int(n))
                    elif isinstance(n, str) and n.strip().lstrip("-").isdigit():
                        normalized.append(int(n.strip()))
                if normalized:
                    nums = normalized
            parsed["nums"] = nums

        return parsed

    return parsed


def main():
    endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318")
    base_url = os.environ.get("LOCAL_OLLAMA_BASE_URL", "http://localhost:11434")
    model = os.environ.get("LOCAL_LLM_MODEL", "llama3.2:3b")

    print(f"OTLP endpoint: {endpoint}")
    print(f"Local model endpoint: {base_url}")
    print(f"Local model: {model}")

    os.environ.setdefault(
        "OTEL_RESOURCE_ATTRIBUTES",
        "agentevals.eval_set_id=langchain_local_ollama_eval,agentevals.session_name=langchain-ollama-zero-code",
    )

    resource = Resource.create()

    tracer_provider = TracerProvider(resource=resource)
    tracer_provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(), schedule_delay_millis=1000))
    trace.set_tracer_provider(tracer_provider)

    logger_provider = LoggerProvider(resource=resource)
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporter(), schedule_delay_millis=1000))
    set_logger_provider(logger_provider)

    OllamaInstrumentor().instrument()

    llm = ChatOllama(
        model=model,
        temperature=0.0,
        base_url=base_url,
    )
    tools = [roll_die, check_prime]
    llm_with_tools = llm.bind_tools(tools)

    test_queries = [
        "Hi! Can you help me?",
        "Roll a 20-sided die for me",
        "Is the number you rolled prime?",
    ]

    messages = []

    for i, query in enumerate(test_queries, 1):
        print(f"\n[{i}/{len(test_queries)}] User: {query}")
        messages.append(HumanMessage(content=query))

        max_iterations = 5
        for _ in range(max_iterations):
            response = llm_with_tools.invoke(messages)
            messages.append(response)

            if not response.tool_calls:
                print(f"     Agent: {response.content}")
                break

            for tool_call in response.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                tool_call_id = tool_call.get("id", f"tool-call-{tool_name}")
                normalized_args = _normalize_tool_args(tool_name, tool_args)

                selected_tool = {t.name: t for t in tools}.get(tool_name)
                if selected_tool:
                    try:
                        tool_result = selected_tool.invoke(normalized_args)
                    except Exception as exc:
                        tool_result = {
                            "isError": True,
                            "error": str(exc),
                            "tool_name": tool_name,
                            "args": normalized_args,
                        }

                    tool_content = json.dumps(tool_result) if isinstance(tool_result, dict) else str(tool_result)
                    messages.append(ToolMessage(content=tool_content, tool_call_id=tool_call_id))
                else:
                    messages.append(
                        ToolMessage(
                            content=json.dumps({"isError": True, "error": f"Unknown tool: {tool_name}"}),
                            tool_call_id=tool_call_id,
                        )
                    )
        else:
            print("     Agent: [Max iterations reached]")

    print()
    tracer_provider.force_flush()
    logger_provider.force_flush()
    print("All traces and logs flushed to OTLP receiver.")


if __name__ == "__main__":
    main()
