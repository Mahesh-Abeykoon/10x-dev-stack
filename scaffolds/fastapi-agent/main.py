from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os

# 🚀 10x-Performance FastAPI Template
# Optimized for AI Agents (Stateless, Async, Typed)

app = FastAPI(title="AI Agent Backend", version="1.0.0")

class AgentRequest(BaseModel):
    query: str
    context: dict = {}

class AgentResponse(BaseModel):
    answer: str
    confidence: float

@app.get("/health")
async def health_check():
    """Keep-alive endpoint for cloud deployment"""
    return {"status": "ok", "version": "1.0.0"}

@app.post("/v1/agent/run", response_model=AgentResponse)
async def run_agent(request: AgentRequest):
    """
    Main entry point for your agent.
    Use Async functions to handle LLM API calls without blocking.
    """
    try:
        # TODO: Call your LangChain/OpenAI logic here
        return AgentResponse(
            answer=f"Processed query: {request.query}", 
            confidence=0.99
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Use standard port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
