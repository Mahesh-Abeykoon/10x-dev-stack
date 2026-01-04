# 🏗️ Scaffold Library

Stop wasting time searching for "best practice" config files. Copy-paste these into your project to get 10x performance immediately.

## ⚡ optimized-vite-react
**Path:** `scaffolds/vite-react-optimized/`
**Use for:** Any new React project.

*   `vite.config.ts`: Pre-configured with chunk splitting (manualChunks) for smaller bundles, and 'esnext' target for performance.
*   `tsconfig.json`: Strict mode enabled (makes AI less likely to hallucinate types).

## 🐍 agentic-fastapi (Python)
**Path:** `scaffolds/fastapi-agent/`
**Use for:** Production-ready AI Agent backend.

*   **⚡ Async Streaming**: Real-time token streaming (`/v1/agent/stream`) for snappy UI.
*   **🧠 Memory Service**: Built-in chat history/session management (in-memory, extensible to Redis).
*   **🛡️ Enterprise Secure**: API Key authentication and request logging middleware included.
*   **🤖 LLM Agnostic**: logical separation of `LLMService` (currently OpenAI) from your business logic.
*   **🧰 Tooling Ready**: Pre-built `BaseTool` structure for function calling.
*   **⚙️ Type-Safe Config**: Pydantic-based configuration management.
