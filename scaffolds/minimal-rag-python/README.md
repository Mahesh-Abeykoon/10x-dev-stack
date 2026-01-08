# 🧠 Minimal Local RAG

A heavily simplified "Chat with your Data" implementation using 100% local AI.

**Stack:**
- **Ollama**: For LLM (Llama3) and Embeddings (Nomic).
- **LanceDB**: Local, high-performance vector database (file-based).
- **Rich**: For a beautiful terminal UI.

## 🛠️ Prereqs

1. Install **Ollama** (ollama.com).
2. Pull the models:
   ```bash
   ollama pull llama3
   ollama pull nomic-embed-text
   ```

## 🚀 Usage

1. **Install Deps:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ingest a Document:**
   ```bash
   python rag.py my-contract.pdf
   ```

3. **Chat:**
   The script will automatically enter chat mode after ingestion. To chat later without re-ingesting:
   ```bash
   python rag.py
   ```
