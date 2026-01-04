from typing import List, Dict, Optional
from pydantic import BaseModel
import time
from uuid import uuid4

class Message(BaseModel):
    role: str  # 'user', 'assistant', 'system'
    content: str
    timestamp: float = Field(default_factory=time.time)

class Session(BaseModel):
    session_id: str
    messages: List[Message] = []
    metadata: Dict[str, Any] = {}

class MemoryService:
    """
    A service to manage conversation history.
    Currently uses in-memory storage. 
    TODO: Replace with Redis/Postgres for production persistence.
    """
    def __init__(self):
        self._storage: Dict[str, Session] = {}

    async def get_session(self, session_id: str) -> Session:
        if session_id not in self._storage:
            self._storage[session_id] = Session(session_id=session_id)
        return self._storage[session_id]

    async def add_message(self, session_id: str, role: str, content: str):
        session = await self.get_session(session_id)
        msg = Message(role=role, content=content)
        session.messages.append(msg)
        return msg

    async def get_history(self, session_id: str) -> List[Message]:
        session = await self.get_session(session_id)
        return session.messages
