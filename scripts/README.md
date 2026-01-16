# 🛠️ 10x Dev Stack Scripts

Utility scripts to enhance your development workflow.

## Scaffold Copier

Quickly copy any scaffold to start a new project.

### Usage

```powershell
# Copy a scaffold to a new directory
.\scripts\copy-scaffold.ps1 vite-react-optimized my-new-project

# Copy FastAPI scaffold
.\scripts\copy-scaffold.ps1 fastapi-agent my-api
```

### Available Scaffolds

- `vite-react-optimized` - React frontend
- `fastapi-agent` - Python API
- `minimal-rag-python` - AI RAG system
- `mcp-server-starter` - Model Context Protocol
- `nextjs-app` - Full-stack Next.js
- `express-api` - Node.js API

The script will automatically tell you the next steps (install dependencies, run dev server, etc.).