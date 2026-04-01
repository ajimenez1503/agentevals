2026-04-01T07:13:11.014Z	info	Logs	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs", "resource logs": 1, "log records": 1}
2026-04-01T07:13:11.017Z	info	ResourceLog #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeLogs #0
ScopeLogs SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
LogRecord #0
ObservedTimestamp: 2026-04-01 07:13:10.138742 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Hi! Can you help me?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: a7e2722c0a36d000e8df425e350999d0
Span ID: 24bdac1671f0c883
Flags: 1
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs"}
2026-04-01T07:13:13.034Z	info	Logs	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs", "resource logs": 1, "log records": 10}
2026-04-01T07:13:13.034Z	info	Traces	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces", "resource spans": 1, "spans": 2}
2026-04-01T07:13:13.034Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
Span #0
    Trace ID       : a7e2722c0a36d000e8df425e350999d0
    Parent ID      :
    ID             : 24bdac1671f0c883
    Name           : chat llama3.2:3b
    Kind           : Client
    Start time     : 2026-04-01 07:13:10.138724 +0000 UTC
    End time       : 2026-04-01 07:13:12.199041 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.system: Str(openai)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> gen_ai.request.temperature: Double(0)
     -> server.address: Str(localhost)
     -> server.port: Int(11434)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> gen_ai.response.finish_reasons: Slice(["tool_calls"])
     -> gen_ai.response.id: Str(chatcmpl-159)
     -> gen_ai.usage.input_tokens: Int(192)
     -> gen_ai.usage.output_tokens: Int(18)
Span #1
    Trace ID       : 731be334eec15abffb8f85bfd5c1e603
    Parent ID      :
    ID             : 9a6d4550888f17ae
    Name           : chat llama3.2:3b
    Kind           : Client
    Start time     : 2026-04-01 07:13:12.201288 +0000 UTC
    End time       : 2026-04-01 07:13:12.783971 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.system: Str(openai)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> gen_ai.request.temperature: Double(0)
     -> server.address: Str(localhost)
     -> server.port: Int(11434)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> gen_ai.response.finish_reasons: Slice(["stop"])
     -> gen_ai.response.id: Str(chatcmpl-910)
     -> gen_ai.usage.input_tokens: Int(120)
     -> gen_ai.usage.output_tokens: Int(20)
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
2026-04-01T07:13:13.035Z	info	ResourceLog #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeLogs #0
ScopeLogs SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
LogRecord #0
ObservedTimestamp: 2026-04-01 07:13:12.198811 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.choice
Body: Map({"finish_reason":"tool_calls","index":0,"message":{"role":"assistant","tool_calls":[{"function":{"arguments":"{\"sides\":6}","name":"roll_die"},"id":"call_bnerapmq","type":"function"}]}})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: a7e2722c0a36d000e8df425e350999d0
Span ID: 24bdac1671f0c883
Flags: 1
LogRecord #1
ObservedTimestamp: 2026-04-01 07:13:12.201304 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Hi! Can you help me?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 731be334eec15abffb8f85bfd5c1e603
Span ID: 9a6d4550888f17ae
Flags: 1
LogRecord #2
ObservedTimestamp: 2026-04-01 07:13:12.201335 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 6}","name":"roll_die"},"id":"call_bnerapmq","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 731be334eec15abffb8f85bfd5c1e603
Span ID: 9a6d4550888f17ae
Flags: 1
LogRecord #3
ObservedTimestamp: 2026-04-01 07:13:12.201352 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 6, \"result\": 5, \"message\": \"Rolled a 5 on a 6-sided die\"}","id":"call_bnerapmq"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 731be334eec15abffb8f85bfd5c1e603
Span ID: 9a6d4550888f17ae
Flags: 1
LogRecord #4
ObservedTimestamp: 2026-04-01 07:13:12.783862 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.choice
Body: Map({"finish_reason":"stop","index":0,"message":{"content":"You rolled a 5 on a 6-sided die. Would you like to roll again?","role":"assistant"}})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 731be334eec15abffb8f85bfd5c1e603
Span ID: 9a6d4550888f17ae
Flags: 1
LogRecord #5
ObservedTimestamp: 2026-04-01 07:13:12.786093 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Hi! Can you help me?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 5b3080afe42733a1e0e5839f9352aa73
Span ID: 5021e97b4fc21e9c
Flags: 1
LogRecord #6
ObservedTimestamp: 2026-04-01 07:13:12.786247 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 6}","name":"roll_die"},"id":"call_bnerapmq","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 5b3080afe42733a1e0e5839f9352aa73
Span ID: 5021e97b4fc21e9c
Flags: 1
LogRecord #7
ObservedTimestamp: 2026-04-01 07:13:12.786297 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 6, \"result\": 5, \"message\": \"Rolled a 5 on a 6-sided die\"}","id":"call_bnerapmq"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 5b3080afe42733a1e0e5839f9352aa73
Span ID: 5021e97b4fc21e9c
Flags: 1
LogRecord #8
ObservedTimestamp: 2026-04-01 07:13:12.786339 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"content":"You rolled a 5 on a 6-sided die. Would you like to roll again?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 5b3080afe42733a1e0e5839f9352aa73
Span ID: 5021e97b4fc21e9c
Flags: 1
LogRecord #9
ObservedTimestamp: 2026-04-01 07:13:12.78638 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Roll a 20-sided die for me"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 5b3080afe42733a1e0e5839f9352aa73
Span ID: 5021e97b4fc21e9c
Flags: 1
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs"}
2026-04-01T07:13:14.039Z	info	Logs	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs", "resource logs": 1, "log records": 8}
2026-04-01T07:13:14.040Z	info	ResourceLog #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeLogs #0
ScopeLogs SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
LogRecord #0
ObservedTimestamp: 2026-04-01 07:13:13.443974 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.choice
Body: Map({"finish_reason":"tool_calls","index":0,"message":{"role":"assistant","tool_calls":[{"function":{"arguments":"{\"sides\":20}","name":"roll_die"},"id":"call_h1cv6x49","type":"function"}]}})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 5b3080afe42733a1e0e5839f9352aa73
Span ID: 5021e97b4fc21e9c
Flags: 1
LogRecord #1
ObservedTimestamp: 2026-04-01 07:13:13.445678 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Hi! Can you help me?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
LogRecord #2
ObservedTimestamp: 2026-04-01 07:13:13.445712 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 6}","name":"roll_die"},"id":"call_bnerapmq","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
LogRecord #3
ObservedTimestamp: 2026-04-01 07:13:13.445727 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 6, \"result\": 5, \"message\": \"Rolled a 5 on a 6-sided die\"}","id":"call_bnerapmq"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
LogRecord #4
ObservedTimestamp: 2026-04-01 07:13:13.44574 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"content":"You rolled a 5 on a 6-sided die. Would you like to roll again?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
LogRecord #5
ObservedTimestamp: 2026-04-01 07:13:13.445751 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Roll a 20-sided die for me"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
LogRecord #6
ObservedTimestamp: 2026-04-01 07:13:13.445764 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 20}","name":"roll_die"},"id":"call_h1cv6x49","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
LogRecord #7
ObservedTimestamp: 2026-04-01 07:13:13.445774 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 20, \"result\": 9, \"message\": \"Rolled a 9 on a 20-sided die\"}","id":"call_h1cv6x49"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs"}
2026-04-01T07:13:14.039Z	info	Traces	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces", "resource spans": 1, "spans": 1}
2026-04-01T07:13:14.040Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
Span #0
    Trace ID       : 5b3080afe42733a1e0e5839f9352aa73
    Parent ID      :
    ID             : 5021e97b4fc21e9c
    Name           : chat llama3.2:3b
    Kind           : Client
    Start time     : 2026-04-01 07:13:12.786045 +0000 UTC
    End time       : 2026-04-01 07:13:13.444096 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.system: Str(openai)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> gen_ai.request.temperature: Double(0)
     -> server.address: Str(localhost)
     -> server.port: Int(11434)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> gen_ai.response.finish_reasons: Slice(["tool_calls"])
     -> gen_ai.response.id: Str(chatcmpl-401)
     -> gen_ai.usage.input_tokens: Int(285)
     -> gen_ai.usage.output_tokens: Int(18)
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
2026-04-01T07:13:15.054Z	info	Traces	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces", "resource spans": 1, "spans": 2}
2026-04-01T07:13:15.055Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
Span #0
    Trace ID       : 553b8b56445253a1d6616c692ac27b97
    Parent ID      :
    ID             : 12c3c99f64ea6b8a
    Name           : chat llama3.2:3b
    Kind           : Client
    Start time     : 2026-04-01 07:13:13.445668 +0000 UTC
    End time       : 2026-04-01 07:13:14.032079 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.system: Str(openai)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> gen_ai.request.temperature: Double(0)
     -> server.address: Str(localhost)
     -> server.port: Int(11434)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> gen_ai.response.finish_reasons: Slice(["stop"])
     -> gen_ai.response.id: Str(chatcmpl-45)
     -> gen_ai.usage.input_tokens: Int(213)
     -> gen_ai.usage.output_tokens: Int(20)
Span #1
    Trace ID       : f7b06c49e9abac4f6e05238605ebe930
    Parent ID      :
    ID             : c8c047b3155acf8a
    Name           : chat llama3.2:3b
    Kind           : Client
    Start time     : 2026-04-01 07:13:14.035205 +0000 UTC
    End time       : 2026-04-01 07:13:14.690562 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.system: Str(openai)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> gen_ai.request.temperature: Double(0)
     -> server.address: Str(localhost)
     -> server.port: Int(11434)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> gen_ai.response.finish_reasons: Slice(["tool_calls"])
     -> gen_ai.response.id: Str(chatcmpl-567)
     -> gen_ai.usage.input_tokens: Int(377)
     -> gen_ai.usage.output_tokens: Int(18)
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
2026-04-01T07:13:15.055Z	info	Logs	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs", "resource logs": 1, "log records": 22}
2026-04-01T07:13:15.059Z	info	ResourceLog #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeLogs #0
ScopeLogs SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
LogRecord #0
ObservedTimestamp: 2026-04-01 07:13:14.031927 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.choice
Body: Map({"finish_reason":"stop","index":0,"message":{"content":"You rolled a 9 on a 20-sided die. Would you like to roll again?","role":"assistant"}})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 553b8b56445253a1d6616c692ac27b97
Span ID: 12c3c99f64ea6b8a
Flags: 1
LogRecord #1
ObservedTimestamp: 2026-04-01 07:13:14.03523 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Hi! Can you help me?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #2
ObservedTimestamp: 2026-04-01 07:13:14.035316 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 6}","name":"roll_die"},"id":"call_bnerapmq","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #3
ObservedTimestamp: 2026-04-01 07:13:14.03536 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 6, \"result\": 5, \"message\": \"Rolled a 5 on a 6-sided die\"}","id":"call_bnerapmq"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #4
ObservedTimestamp: 2026-04-01 07:13:14.035402 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"content":"You rolled a 5 on a 6-sided die. Would you like to roll again?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #5
ObservedTimestamp: 2026-04-01 07:13:14.035511 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Roll a 20-sided die for me"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #6
ObservedTimestamp: 2026-04-01 07:13:14.035556 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 20}","name":"roll_die"},"id":"call_h1cv6x49","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #7
ObservedTimestamp: 2026-04-01 07:13:14.035596 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 20, \"result\": 9, \"message\": \"Rolled a 9 on a 20-sided die\"}","id":"call_h1cv6x49"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #8
ObservedTimestamp: 2026-04-01 07:13:14.035637 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"content":"You rolled a 9 on a 20-sided die. Would you like to roll again?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #9
ObservedTimestamp: 2026-04-01 07:13:14.035676 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Is the number you rolled prime?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #10
ObservedTimestamp: 2026-04-01 07:13:14.690397 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.choice
Body: Map({"finish_reason":"tool_calls","index":0,"message":{"role":"assistant","tool_calls":[{"function":{"arguments":"{\"nums\":\"[9]\"}","name":"check_prime"},"id":"call_r7d20u4q","type":"function"}]}})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: f7b06c49e9abac4f6e05238605ebe930
Span ID: c8c047b3155acf8a
Flags: 1
LogRecord #11
ObservedTimestamp: 2026-04-01 07:13:14.692825 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Hi! Can you help me?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #12
ObservedTimestamp: 2026-04-01 07:13:14.692915 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 6}","name":"roll_die"},"id":"call_bnerapmq","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #13
ObservedTimestamp: 2026-04-01 07:13:14.692967 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 6, \"result\": 5, \"message\": \"Rolled a 5 on a 6-sided die\"}","id":"call_bnerapmq"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #14
ObservedTimestamp: 2026-04-01 07:13:14.69302 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"content":"You rolled a 5 on a 6-sided die. Would you like to roll again?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #15
ObservedTimestamp: 2026-04-01 07:13:14.693069 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Roll a 20-sided die for me"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #16
ObservedTimestamp: 2026-04-01 07:13:14.693117 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"sides\": 20}","name":"roll_die"},"id":"call_h1cv6x49","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #17
ObservedTimestamp: 2026-04-01 07:13:14.693155 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"sides\": 20, \"result\": 9, \"message\": \"Rolled a 9 on a 20-sided die\"}","id":"call_h1cv6x49"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #18
ObservedTimestamp: 2026-04-01 07:13:14.693194 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"content":"You rolled a 9 on a 20-sided die. Would you like to roll again?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #19
ObservedTimestamp: 2026-04-01 07:13:14.693232 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.user.message
Body: Map({"content":"Is the number you rolled prime?"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #20
ObservedTimestamp: 2026-04-01 07:13:14.693273 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.assistant.message
Body: Map({"tool_calls":[{"function":{"arguments":"{\"nums\": [9]}","name":"check_prime"},"id":"call_r7d20u4q","type":"function"}]})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
LogRecord #21
ObservedTimestamp: 2026-04-01 07:13:14.693311 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.tool.message
Body: Map({"content":"{\"results\": {\"9\": false}, \"prime_count\": 0, \"prime_numbers\": []}","id":"call_r7d20u4q"})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs"}
2026-04-01T07:13:15.464Z	info	Traces	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces", "resource spans": 1, "spans": 1}
2026-04-01T07:13:15.464Z	info	Logs	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs", "resource logs": 1, "log records": 1}
2026-04-01T07:13:15.466Z	info	ResourceLog #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeLogs #0
ScopeLogs SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
LogRecord #0
ObservedTimestamp: 2026-04-01 07:13:15.273205 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
EventName: gen_ai.choice
Body: Map({"finish_reason":"stop","index":0,"message":{"content":"The number 9 is not a prime number. Would you like to roll again or ask another question?","role":"assistant"}})
Attributes:
     -> gen_ai.system: Str(openai)
Trace ID: 7ba8ad2fb4d10b1a01d3963763cf00af
Span ID: 8227a9e9a87c83ae
Flags: 1
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "logs"}
2026-04-01T07:13:15.466Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL: https://opentelemetry.io/schemas/1.30.0
InstrumentationScope opentelemetry.instrumentation.openai_v2
Span #0
    Trace ID       : 7ba8ad2fb4d10b1a01d3963763cf00af
    Parent ID      :
    ID             : 8227a9e9a87c83ae
    Name           : chat llama3.2:3b
    Kind           : Client
    Start time     : 2026-04-01 07:13:14.692798 +0000 UTC
    End time       : 2026-04-01 07:13:15.273336 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> gen_ai.operation.name: Str(chat)
     -> gen_ai.system: Str(openai)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> gen_ai.request.temperature: Double(0)
     -> server.address: Str(localhost)
     -> server.port: Int(11434)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> gen_ai.response.finish_reasons: Slice(["stop"])
     -> gen_ai.response.id: Str(chatcmpl-685)
     -> gen_ai.usage.input_tokens: Int(297)
     -> gen_ai.usage.output_tokens: Int(22)
	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
^C2026-04-01T07:13:23.487Z	info	otelcol@v0.147.0/collector.go:375	Received signal from OS	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "signal": "interrupt"}
2026-04-01T07:13:23.488Z	info	service@v0.147.0/service.go:278	Starting shutdown...	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}}
2026-04-01T07:13:23.490Z	info	extensions/extensions.go:68	Stopping extensions...	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}}
2026-04-01T07:13:23.490Z	info	service@v0.147.0/service.go:292	Shutdown complete.	{"resource": {"service.instance.id": "2d7c8d5c-98e2-40d1-9695-a69c18de9afe", "service.name": "otelcol-contrib", "service.version": "0.147.0"}}
(.venv)  antonjim@ANTONJIM-M-77K2  ~/Documents/dev/github/ajimenez1503/soloio/agentevals   main ± 