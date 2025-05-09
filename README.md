# Example App of OpenTelemetry Instrumentation for Valkey

This example application uses Docker Compose to start Valkey (a Redis-compatible server) and Jaeger with OTLP support. It demonstrates how to instrument Valkey operations with OpenTelemetry and export traces to Jaeger via the OTLP gRPC exporter.

## Directory Structure

```
.
├── compose.yaml         # Docker Compose configuration for Valkey and Jaeger
├── pyproject.toml       # Poetry project configuration
├── app.py               # Sample application code
└── README.md            # This document
```

## Prerequisites

- Docker & Docker Compose
- Python 3.13
- Poetry

## Setup Instructions

1. Clone or check out the repository.
2. Install dependencies with Poetry:

    ```bash
    poetry install
    ```

3. Start Valkey and Jaeger with Docker Compose:

    ```bash
    docker-compose up -d
    ```

4. Enter the Poetry environment and run the app:
  
    ```bash
    poetry run start
    ```

5. Open Jaeger UI:
    Visit http://localhost:16686 in your browser and select the valkey-example-app service to view traces.
