from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn
import asyncio
from typing import List, Optional

from config import get_settings
from middleware.logger import RequestLoggerMiddleware
from middleware.auth import SecurityMiddleware
from services.memory import MemoryService
from services.llm import LLMService
from tools.base import BaseTool

# 🚀 10x-Performance FastAPI Template
# Optimized for AI Agents (Stateless, Async, Typed)

settings = get_settings()

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# 1. Add Middleware
app.add_middleware(SecurityMiddleware) # 🔒 Secure first
app.add_middleware(RequestLoggerMiddleware) # 📝 Log after

# Initialize Services
memory_service = MemoryService()
llm_service = LLMService()

class AgentRequest(BaseModel):
    query: str
    session_id: str = "default" # For memory context
    context: dict = {}

class AgentResponse(BaseModel):
    answer: str
    confidence: float
    used_tools: List[str] = []

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
    Integrates Memory, Tooling, and LLMs.
    """
    try:
        # A. Retrieve History
        history = await memory_service.get_history(request.session_id)
        
        # B. Add User Query to Memory
        await memory_service.add_message(request.session_id, "user", request.query)

        # C. Call LLM Service
        # We construct a simple prompt with history context
        history_text = "\n".join([f"{msg.role}: {msg.content}" for msg in history[-5:]])
        full_prompt = f"History:\n{history_text}\n\nUser: {request.query}"
        
        response_text = await llm_service.get_response(full_prompt)
        
        # D. Add Assistant Response to Memory
        await memory_service.add_message(request.session_id, "assistant", response_text)

        return AgentResponse(
            answer=response_text, 
            confidence=0.99,
            used_tools=["llm_service"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/v1/agent/stream")
async def stream_agent(request: AgentRequest):
    """
    Streaming endpoint.
    """
    return StreamingResponse(
        llm_service.stream_response(request.query), 
        media_type="text/plain"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
