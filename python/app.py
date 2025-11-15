from flask import Flask, request, jsonify
from time import sleep
from opentelemetry import trace
from random import randint
from opentelemetry.sdk.trace import TracerProvider
import logging
#from opentelemetry.sdk.trace.export import (
#    BatchSpanProcessor,
#    ConsoleSpanExporter,
#)
#from opentelemetry.semconv.trace import SpanAttributes
#from opentelemetry.sdk.metrics import MeterProvider

#work_counter = meter.create_counter(
#    "work.counter", unit="1", description="Counts the amount of work done"
#)


# ==== Pour Memo propagateur Datadog ====
#from opentelemetry.propagate import set_global_textmap
#from opentelemetry.propagators.datadog import DatadogPropagator

#set_global_textmap(DatadogPropagator())

# Acquire a tracer
tracer = trace.get_tracer("demo.main")

logger = logging.getLogger('mon_logger')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def hello_world():
    with tracer.start_as_current_span("home_render") as span:
        logger.info('hello world')
        res = randint(1, 6)
        span.set_attribute("roll.value", res)
        print(request.args.get("param"))
        with tracer.start_as_current_span("child") as child:
            # do some work that 'child' tracks
            print("doing some nested work...")
            child.add_event("Gonna try it!")
            child.add_event("Gonna try it!")
            # the nested span is closed when it's out of scope
        return "<p>Hello, World!</p>"


@app.route("/sleep")
@tracer.start_as_current_span("sleep_render")
def sleep_route():
    res = randint(1, 3)
    sleep(res)
    span = trace.get_current_span()
    span.set_attribute("sleep.value", res)
    return "<p>End sleep, wake up!</p>"


@app.route("/2")
@tracer.start_as_current_span("link")
def hello_world2():
    span = trace.get_current_span()
    ctx = span.get_span_context()
    span.add_event("link: Gonna try it!")

    link_from_span_1 = trace.Link(ctx)

    with tracer.start_as_current_span("span-2", links=[link_from_span_1]) as l:
        l.add_event("link2: Gonna try it!")
        # Do something that 'span-2' tracks.
        # The link in 'span-2' is causally associated it with the 'span-1',
        # but it is not a child span.


    return "<p>link!</p>"


def link2():
    with tracer.start_as_current_span("link2") as span:
        res = randint(1, 6)
        span.set_attribute("roll.value", res)
        print(request.args.get("param"))
        with tracer.start_as_current_span("child") as child:
            # do some work that 'child' tracks
            print("doing some nested work...")
            child.add_event("Gonna try it!")
            # the nested span is closed when it's out of scope
        return "<p>Hello, World!</p>"


if __name__ == "__main__":
  app.run(port=8080, host="0.0.0.0")
