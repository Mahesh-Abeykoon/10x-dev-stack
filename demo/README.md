# 🚀 Quick Start Demo

This demo shows how to get started with the 10x Dev Stack scaffolds in under 5 minutes.

## Demo: Build an AI-Powered Todo App

### Step 1: Choose Your Stack
For this demo, we'll use:
- **Frontend**: Vite + React + TypeScript
- **Backend**: FastAPI Agent Service
- **AI**: Minimal Local RAG

### Step 2: Copy Scaffolds
```bash
# Copy frontend scaffold
cp -r scaffolds/vite-react-optimized ./todo-frontend

# Copy backend scaffold
cp -r scaffolds/fastapi-agent ./todo-backend

# Copy RAG scaffold
cp -r scaffolds/minimal-rag-python ./todo-rag
```

### Step 3: Setup & Run
```bash
# Frontend
cd todo-frontend && npm install && npm run dev

# Backend
cd todo-backend && pip install -r requirements.txt && python main.py

# RAG (in another terminal)
cd todo-rag && pip install -r requirements.txt && python rag.py
```

### Step 4: Integrate AI
The scaffolds are pre-configured for AI integration. Just add your AI logic to the ready-made endpoints and components.

## 🎯 What You'll Get

- ✅ Modern, scalable architecture
- ✅ AI-ready endpoints and components
- ✅ Optimized for Cursor/Windsurf development
- ✅ Production-ready configurations

## 📚 Learn More

Check out the [scaffolds README](scaffolds/README.md) for detailed setup instructions for each template.