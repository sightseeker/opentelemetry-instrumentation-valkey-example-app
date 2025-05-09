import os
import time

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.valkey import ValkeyInstrumentor
import valkey

def init_tracer():
  resource = Resource.create({"service.name": "valkey-sample-app"})
  provider = TracerProvider(resource=resource)
  otlp_exporter = OTLPSpanExporter(
      endpoint=os.getenv("OTLP_EXPORTER_ENDPOINT", "localhost:4317"),
      insecure=True,
  )
  span_processor = BatchSpanProcessor(otlp_exporter)
  provider.add_span_processor(span_processor)
  trace.set_tracer_provider(provider)

def main():
  init_tracer()
  ValkeyInstrumentor().instrument()

  client = valkey.Valkey(host="localhost", port=6379, decode_responses=True)

  tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("valkey_demo"):
      client.set("foo", "bar")
      value = client.get("foo")
      print(f"GET foo -> {value}")

  time.sleep(5)
  print("Done.")

if __name__ == "__main__":
  main()
