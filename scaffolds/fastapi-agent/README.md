# 🤖 FastAPI Agent Scaffold

A production-ready, high-performance scaffold for building AI Agents with Python.

## 🚀 Features

- **FastAPI**: Async, high-performance, and auto-documented.
- **Streaming**: Native support for real-time token streaming (`/v1/agent/stream`).
- **Memory**: Built-in session-based conversation history.
- **LLM Agnostic**: Clean separation of concerns; easily swap OpenAI for Anthropic/Local.
- **Dockerized**: specific `Dockerfile` tuned for python microservices.
- **Type-Safe**: Full Pydantic v2 integration for config and data validation.

## 📦 Setup

1. **Install**
   ```bash
   make install
   ```

2. **Environment**
   Copy `.env.example` to `.env` and set your API keys.
   ```bash
   cp .env.example .env
   ```

3. **Run Locally**
   ```bash
   make dev
   ```

4. **Run with Docker**
   ```bash
   make build
   make run
   ```

## 🧪 Testing

Run the test suite:
```bash
make test
```

## 📂 Structure

- `main.py`: Entry point and API routes.
- `services/`: Core business logic (LLM, Memory).
- `middleware/`: Auth, Logging, etc.
- `tools/`: Function calling definitions (Tools).
- `config.py`: Environment configuration.
