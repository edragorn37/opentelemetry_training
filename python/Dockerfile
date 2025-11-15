FROM python:3

WORKDIR /app

RUN pip install "flask<3" "werkzeug<3"
RUN pip install opentelemetry-distro opentelemetry-exporter-otlp opentelemetry-api opentelemetry-sdk opentelemetry-semantic-conventions
RUN opentelemetry-bootstrap -a install


ADD ./app.py .

ENV OTEL_SERVICE_NAME=demo
ENV OTEL_TRACES_EXPORTER=console,otlp
ENV OTEL_METRICS_EXPORTER=console,otlp
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317

CMD ["opentelemetry-instrument", "python", "app.py"]
