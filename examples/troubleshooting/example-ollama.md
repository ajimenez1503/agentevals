Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL:
InstrumentationScope opentelemetry.instrumentation.ollama 0.57.0
Span #0
    Trace ID       : d43842922319fd9cbf9829e702e4124d
    Parent ID      :
    ID             : 2b7263989e73c210
    Name           : ollama.chat
    Kind           : Client
    Start time     : 2026-04-01 07:28:42.293099 +0000 UTC
    End time       : 2026-04-01 07:28:44.170246 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> llm.request.type: Str(chat)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> llm.is_streaming: Bool(true)
     -> gen_ai.prompt.0.role: Str(user)
     -> gen_ai.prompt.0.content: Str(Hi! Can you help me?)
     -> llm.request.functions.0.name: Str(roll_die)
     -> llm.request.functions.0.description: Str(Roll a die with a specified number of sides.)
     -> llm.request.functions.0.parameters: Str({"type": "object", "properties": {"sides": {"type": "integer"}}})
     -> llm.request.functions.1.name: Str(check_prime)
     -> llm.request.functions.1.description: Str(Check if numbers are prime.)
     -> llm.request.functions.1.parameters: Str({"type": "object", "required": ["nums"], "properties": {"nums": {"type": "array", "items": {"type": "integer"}}}})
     -> gen_ai.completion.0.role: Str(assistant)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> llm.usage.total_tokens: Int(210)
     -> gen_ai.usage.output_tokens: Int(18)
     -> gen_ai.usage.input_tokens: Int(192)
     -> gen_ai.system: Str(Ollama)
	{"resource": {"service.instance.id": "5ae43280-e76f-4df3-8226-64ee9b933e45", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
2026-04-01T07:28:45.403Z	info	Traces	{"resource": {"service.instance.id": "5ae43280-e76f-4df3-8226-64ee9b933e45", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces", "resource spans": 1, "spans": 1}
2026-04-01T07:28:45.403Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL:
InstrumentationScope opentelemetry.instrumentation.ollama 0.57.0
Span #0
    Trace ID       : 5cb2f7c18e78f026e15cf0ced4d6904e
    Parent ID      :
    ID             : bb8ef41e144b2679
    Name           : ollama.chat
    Kind           : Client
    Start time     : 2026-04-01 07:28:44.173369 +0000 UTC
    End time       : 2026-04-01 07:28:44.760511 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> llm.request.type: Str(chat)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> llm.is_streaming: Bool(true)
     -> gen_ai.prompt.0.role: Str(user)
     -> gen_ai.prompt.0.content: Str(Hi! Can you help me?)
     -> gen_ai.prompt.1.role: Str(assistant)
     -> gen_ai.prompt.1.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.1.tool_calls.0.arguments: Str({"sides": 6})
     -> gen_ai.prompt.2.role: Str(tool)
     -> gen_ai.prompt.2.content: Str({"sides": 6, "result": 4, "message": "Rolled a 4 on a 6-sided die"})
     -> llm.request.functions.0.name: Str(roll_die)
     -> llm.request.functions.0.description: Str(Roll a die with a specified number of sides.)
     -> llm.request.functions.0.parameters: Str({"type": "object", "properties": {"sides": {"type": "integer"}}})
     -> llm.request.functions.1.name: Str(check_prime)
     -> llm.request.functions.1.description: Str(Check if numbers are prime.)
     -> llm.request.functions.1.parameters: Str({"type": "object", "required": ["nums"], "properties": {"nums": {"type": "array", "items": {"type": "integer"}}}})
     -> gen_ai.completion.0.content: Str(You rolled a 4 on a 6-sided die. Would you like to roll again?)
     -> gen_ai.completion.0.role: Str(assistant)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> llm.usage.total_tokens: Int(140)
     -> gen_ai.usage.output_tokens: Int(20)
     -> gen_ai.usage.input_tokens: Int(120)
     -> gen_ai.system: Str(Ollama)
	{"resource": {"service.instance.id": "5ae43280-e76f-4df3-8226-64ee9b933e45", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
2026-04-01T07:28:46.416Z	info	Traces	{"resource": {"service.instance.id": "5ae43280-e76f-4df3-8226-64ee9b933e45", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces", "resource spans": 1, "spans": 2}
2026-04-01T07:28:46.417Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL:
InstrumentationScope opentelemetry.instrumentation.ollama 0.57.0
Span #0
    Trace ID       : f9ea7d4ad69153bbc66417c5a1895ab2
    Parent ID      :
    ID             : f247050084ab6286
    Name           : ollama.chat
    Kind           : Client
    Start time     : 2026-04-01 07:28:44.762914 +0000 UTC
    End time       : 2026-04-01 07:28:45.412878 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> llm.request.type: Str(chat)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> llm.is_streaming: Bool(true)
     -> gen_ai.prompt.0.role: Str(user)
     -> gen_ai.prompt.0.content: Str(Hi! Can you help me?)
     -> gen_ai.prompt.1.role: Str(assistant)
     -> gen_ai.prompt.1.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.1.tool_calls.0.arguments: Str({"sides": 6})
     -> gen_ai.prompt.2.role: Str(tool)
     -> gen_ai.prompt.2.content: Str({"sides": 6, "result": 4, "message": "Rolled a 4 on a 6-sided die"})
     -> gen_ai.prompt.3.role: Str(assistant)
     -> gen_ai.prompt.3.content: Str(You rolled a 4 on a 6-sided die. Would you like to roll again?)
     -> gen_ai.prompt.4.role: Str(user)
     -> gen_ai.prompt.4.content: Str(Roll a 20-sided die for me)
     -> llm.request.functions.0.name: Str(roll_die)
     -> llm.request.functions.0.description: Str(Roll a die with a specified number of sides.)
     -> llm.request.functions.0.parameters: Str({"type": "object", "properties": {"sides": {"type": "integer"}}})
     -> llm.request.functions.1.name: Str(check_prime)
     -> llm.request.functions.1.description: Str(Check if numbers are prime.)
     -> llm.request.functions.1.parameters: Str({"type": "object", "required": ["nums"], "properties": {"nums": {"type": "array", "items": {"type": "integer"}}}})
     -> gen_ai.completion.0.role: Str(assistant)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> llm.usage.total_tokens: Int(303)
     -> gen_ai.usage.output_tokens: Int(18)
     -> gen_ai.usage.input_tokens: Int(285)
     -> gen_ai.system: Str(Ollama)
Span #1
    Trace ID       : d411e5438ecc53d13f8e110cfc5ee807
    Parent ID      :
    ID             : 7e4cf21d1e06b6ab
    Name           : ollama.chat
    Kind           : Client
    Start time     : 2026-04-01 07:28:45.415016 +0000 UTC
    End time       : 2026-04-01 07:28:45.990931 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> llm.request.type: Str(chat)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> llm.is_streaming: Bool(true)
     -> gen_ai.prompt.0.role: Str(user)
     -> gen_ai.prompt.0.content: Str(Hi! Can you help me?)
     -> gen_ai.prompt.1.role: Str(assistant)
     -> gen_ai.prompt.1.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.1.tool_calls.0.arguments: Str({"sides": 6})
     -> gen_ai.prompt.2.role: Str(tool)
     -> gen_ai.prompt.2.content: Str({"sides": 6, "result": 4, "message": "Rolled a 4 on a 6-sided die"})
     -> gen_ai.prompt.3.role: Str(assistant)
     -> gen_ai.prompt.3.content: Str(You rolled a 4 on a 6-sided die. Would you like to roll again?)
     -> gen_ai.prompt.4.role: Str(user)
     -> gen_ai.prompt.4.content: Str(Roll a 20-sided die for me)
     -> gen_ai.prompt.5.role: Str(assistant)
     -> gen_ai.prompt.5.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.5.tool_calls.0.arguments: Str({"sides": 20})
     -> gen_ai.prompt.6.role: Str(tool)
     -> gen_ai.prompt.6.content: Str({"sides": 20, "result": 13, "message": "Rolled a 13 on a 20-sided die"})
     -> llm.request.functions.0.name: Str(roll_die)
     -> llm.request.functions.0.description: Str(Roll a die with a specified number of sides.)
     -> llm.request.functions.0.parameters: Str({"type": "object", "properties": {"sides": {"type": "integer"}}})
     -> llm.request.functions.1.name: Str(check_prime)
     -> llm.request.functions.1.description: Str(Check if numbers are prime.)
     -> llm.request.functions.1.parameters: Str({"type": "object", "required": ["nums"], "properties": {"nums": {"type": "array", "items": {"type": "integer"}}}})
     -> gen_ai.completion.0.content: Str(You rolled a 13 on a 20-sided die. Would you like to roll again?)
     -> gen_ai.completion.0.role: Str(assistant)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> llm.usage.total_tokens: Int(233)
     -> gen_ai.usage.output_tokens: Int(20)
     -> gen_ai.usage.input_tokens: Int(213)
     -> gen_ai.system: Str(Ollama)
	{"resource": {"service.instance.id": "5ae43280-e76f-4df3-8226-64ee9b933e45", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
2026-04-01T07:28:47.224Z	info	Traces	{"resource": {"service.instance.id": "5ae43280-e76f-4df3-8226-64ee9b933e45", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces", "resource spans": 1, "spans": 2}
2026-04-01T07:28:47.225Z	info	ResourceSpans #0
Resource SchemaURL:
Resource attributes:
     -> telemetry.sdk.language: Str(python)
     -> telemetry.sdk.name: Str(opentelemetry)
     -> telemetry.sdk.version: Str(1.38.0)
     -> agentevals.eval_set_id: Str(langchain_local_ollama_eval)
     -> agentevals.session_name: Str(langchain-ollama-zero-code)
     -> service.name: Str(unknown_service)
ScopeSpans #0
ScopeSpans SchemaURL:
InstrumentationScope opentelemetry.instrumentation.ollama 0.57.0
Span #0
    Trace ID       : 5aabd1ead1df7f200ffc99368443797d
    Parent ID      :
    ID             : 80072804a3bdb611
    Name           : ollama.chat
    Kind           : Client
    Start time     : 2026-04-01 07:28:45.994496 +0000 UTC
    End time       : 2026-04-01 07:28:46.647071 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> llm.request.type: Str(chat)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> llm.is_streaming: Bool(true)
     -> gen_ai.prompt.0.role: Str(user)
     -> gen_ai.prompt.0.content: Str(Hi! Can you help me?)
     -> gen_ai.prompt.1.role: Str(assistant)
     -> gen_ai.prompt.1.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.1.tool_calls.0.arguments: Str({"sides": 6})
     -> gen_ai.prompt.2.role: Str(tool)
     -> gen_ai.prompt.2.content: Str({"sides": 6, "result": 4, "message": "Rolled a 4 on a 6-sided die"})
     -> gen_ai.prompt.3.role: Str(assistant)
     -> gen_ai.prompt.3.content: Str(You rolled a 4 on a 6-sided die. Would you like to roll again?)
     -> gen_ai.prompt.4.role: Str(user)
     -> gen_ai.prompt.4.content: Str(Roll a 20-sided die for me)
     -> gen_ai.prompt.5.role: Str(assistant)
     -> gen_ai.prompt.5.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.5.tool_calls.0.arguments: Str({"sides": 20})
     -> gen_ai.prompt.6.role: Str(tool)
     -> gen_ai.prompt.6.content: Str({"sides": 20, "result": 13, "message": "Rolled a 13 on a 20-sided die"})
     -> gen_ai.prompt.7.role: Str(assistant)
     -> gen_ai.prompt.7.content: Str(You rolled a 13 on a 20-sided die. Would you like to roll again?)
     -> gen_ai.prompt.8.role: Str(user)
     -> gen_ai.prompt.8.content: Str(Is the number you rolled prime?)
     -> llm.request.functions.0.name: Str(roll_die)
     -> llm.request.functions.0.description: Str(Roll a die with a specified number of sides.)
     -> llm.request.functions.0.parameters: Str({"type": "object", "properties": {"sides": {"type": "integer"}}})
     -> llm.request.functions.1.name: Str(check_prime)
     -> llm.request.functions.1.description: Str(Check if numbers are prime.)
     -> llm.request.functions.1.parameters: Str({"type": "object", "required": ["nums"], "properties": {"nums": {"type": "array", "items": {"type": "integer"}}}})
     -> gen_ai.completion.0.role: Str(assistant)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> llm.usage.total_tokens: Int(395)
     -> gen_ai.usage.output_tokens: Int(18)
     -> gen_ai.usage.input_tokens: Int(377)
     -> gen_ai.system: Str(Ollama)
Span #1
    Trace ID       : de7b7280a2191e770fe3c533144172a6
    Parent ID      :
    ID             : 5e496bf799b99568
    Name           : ollama.chat
    Kind           : Client
    Start time     : 2026-04-01 07:28:46.649387 +0000 UTC
    End time       : 2026-04-01 07:28:47.16431 +0000 UTC
    Status code    : Unset
    Status message :
    DroppedAttributesCount: 0
    DroppedEventsCount: 0
    DroppedLinksCount: 0
Attributes:
     -> llm.request.type: Str(chat)
     -> gen_ai.request.model: Str(llama3.2:3b)
     -> llm.is_streaming: Bool(true)
     -> gen_ai.prompt.0.role: Str(user)
     -> gen_ai.prompt.0.content: Str(Hi! Can you help me?)
     -> gen_ai.prompt.1.role: Str(assistant)
     -> gen_ai.prompt.1.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.1.tool_calls.0.arguments: Str({"sides": 6})
     -> gen_ai.prompt.2.role: Str(tool)
     -> gen_ai.prompt.2.content: Str({"sides": 6, "result": 4, "message": "Rolled a 4 on a 6-sided die"})
     -> gen_ai.prompt.3.role: Str(assistant)
     -> gen_ai.prompt.3.content: Str(You rolled a 4 on a 6-sided die. Would you like to roll again?)
     -> gen_ai.prompt.4.role: Str(user)
     -> gen_ai.prompt.4.content: Str(Roll a 20-sided die for me)
     -> gen_ai.prompt.5.role: Str(assistant)
     -> gen_ai.prompt.5.tool_calls.0.name: Str(roll_die)
     -> gen_ai.prompt.5.tool_calls.0.arguments: Str({"sides": 20})
     -> gen_ai.prompt.6.role: Str(tool)
     -> gen_ai.prompt.6.content: Str({"sides": 20, "result": 13, "message": "Rolled a 13 on a 20-sided die"})
     -> gen_ai.prompt.7.role: Str(assistant)
     -> gen_ai.prompt.7.content: Str(You rolled a 13 on a 20-sided die. Would you like to roll again?)
     -> gen_ai.prompt.8.role: Str(user)
     -> gen_ai.prompt.8.content: Str(Is the number you rolled prime?)
     -> gen_ai.prompt.9.role: Str(assistant)
     -> gen_ai.prompt.9.tool_calls.0.name: Str(check_prime)
     -> gen_ai.prompt.9.tool_calls.0.arguments: Str({"nums": [13]})
     -> gen_ai.prompt.10.role: Str(tool)
     -> gen_ai.prompt.10.content: Str({"results": {"13": true}, "prime_count": 1, "prime_numbers": [13]})
     -> llm.request.functions.0.name: Str(roll_die)
     -> llm.request.functions.0.description: Str(Roll a die with a specified number of sides.)
     -> llm.request.functions.0.parameters: Str({"type": "object", "properties": {"sides": {"type": "integer"}}})
     -> llm.request.functions.1.name: Str(check_prime)
     -> llm.request.functions.1.description: Str(Check if numbers are prime.)
     -> llm.request.functions.1.parameters: Str({"type": "object", "required": ["nums"], "properties": {"nums": {"type": "array", "items": {"type": "integer"}}}})
     -> gen_ai.completion.0.content: Str(Yes, the number 13 is a prime number. Would you like to roll again?)
     -> gen_ai.completion.0.role: Str(assistant)
     -> gen_ai.response.model: Str(llama3.2:3b)
     -> llm.usage.total_tokens: Int(317)
     -> gen_ai.usage.output_tokens: Int(19)
     -> gen_ai.usage.input_tokens: Int(298)
     -> gen_ai.system: Str(Ollama)
	{"resource": {"service.instance.id": "5ae43280-e76f-4df3-8226-64ee9b933e45", "service.name": "otelcol-contrib", "service.version": "0.147.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
