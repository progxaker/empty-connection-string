import pytest
from os import environ
from time import sleep
from opentelemetry import trace
from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor()
tracer = trace.get_tracer("SimpleApp", "1.0")

# Test main function
def test_main():
    main()
    captured = capsys.readouterr()
    assert(captured!="") in captured.out
