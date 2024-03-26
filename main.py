from os import environ
from time import sleep
from opentelemetry import trace
from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor()
tracer = trace.get_tracer("SimpleApp", "1.0")

def main():
    with tracer.start_as_current_span("simple-app") as span:
        sleep(10)
        print (trace.format_trace_id(span.get_span_context().trace_id))

if __name__ == "__main__":
    main()
