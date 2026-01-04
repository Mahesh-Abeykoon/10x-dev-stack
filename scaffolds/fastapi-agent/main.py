from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn
import asyncio
from typing import List, Optional

from config import get_settings
from middleware.logger import RequestLoggerMiddleware
from services.memory import MemoryService
from tools.base import BaseTool

# 🚀 10x-Performance FastAPI Template
# Optimized for AI Agents (Stateless, Async, Typed)

settings = get_settings()

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# 1. Add Middleware (Observability)
app.add_middleware(RequestLoggerMiddleware)

# Initialize Services
memory_service = MemoryService()

class AgentRequest(BaseModel):
    query: str
    session_id: str = "default" # For memory context
    context: dict = {}

class AgentResponse(BaseModel):
    answer: str
    confidence: float
    used_tools: List[str] = []

async def fake_stream_generator(query: str):
    """Simulates an LLM streaming tokens"""
    tokens = ["Thinking", "...", " about", " '", query, "'", ".", " This", " is", " a", " streamed", " response", "."]
    for token in tokens:
        yield token
        await asyncio.sleep(0.1)  # Simulate network latency

@app.get("/health")
async def health_check():
    """Keep-alive endpoint for cloud deployment"""
    return {
        "status": "ok", 
        "version": settings.VERSION,
        "env": settings.ENVIRONMENT
    }

@app.post("/v1/agent/run", response_model=AgentResponse)
async def run_agent(request: AgentRequest):
    """
    Main entry point for your agent.
    Integrates Memory and Tooling.
    """
    try:
        # A. Retrieve History
        history = await memory_service.get_history(request.session_id)
        
        # B. Add User Query to Memory
        await memory_service.add_message(request.session_id, "user", request.query)

        # TODO: C. Call your Logic / LLM with history
        # (This is where you would hydrate your LangChain agent with tools)
        
        response_text = f"Processed query: {request.query}. I have {len(history)} previous messages in context."
        
        # D. Add Assistant Response to Memory
        await memory_service.add_message(request.session_id, "assistant", response_text)

        return AgentResponse(
            answer=response_text, 
            confidence=0.99,
            used_tools=["memory_retriever"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/v1/agent/stream")
async def stream_agent(request: AgentRequest):
    """
    Streaming endpoint.
    """
    # Note: For streaming, you'd usually stream the response into memory 
    # as chunks arrive, then save the full message at the end.
    return StreamingResponse(
        fake_stream_generator(request.query), 
        media_type="text/plain"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
