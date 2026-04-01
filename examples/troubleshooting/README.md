# Troubleshooting OTel Streaming

Use this guide to confirm what your agent is actually sending over OTLP before it reaches agentevals.

## Run Jaeger and collector

1. Create a shared Docker network:

```bash
docker network create otel-net
```

1. Run Jaeger (UI on `http://localhost:16686`):

```bash
docker run --rm -d --name jaeger --network otel-net -p 16686:16686 jaegertracing/all-in-one:latest
```

1. Run OpenTelemetry Collector with debug + Jaeger export:

```bash
docker run --rm -it --network otel-net -p 4318:4318 -v "$(pwd)/examples/troubleshooting/otel-collector-config.yaml:/etc/otelcol-contrib/config.yaml" otel/opentelemetry-collector-contrib:latest
```

Keep this terminal open. You should see debug output as telemetry arrives.

## Point your agent at the collector

In another terminal, run your agent with OTLP endpoint set to the collector:

```bash
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
python examples/zero-code-examples/test2/run.py
```

## View traces in Jaeger

Open `http://localhost:16686`, select service `unknown_service`, and click **Find Traces**.
