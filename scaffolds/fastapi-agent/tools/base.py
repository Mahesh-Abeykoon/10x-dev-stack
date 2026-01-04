from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Any, Dict

class BaseTool(ABC):
    """
    Abstract base class for all tools.
    Agents can use these tools to perform actions.
    """
    name: str = Field(description="The unique name of the tool")
    description: str = Field(description="A description of what the tool does")
    
    @abstractmethod
    async def run(self, input_data: Any) -> Any:
        """
        Execute the tool logic.
        """
        pass
    
    def to_schema(self) -> Dict[str, Any]:
        """
        Returns the JSON schema for the tool, compatible with OpenAI function calling.
        """
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                # In a real impl, you'd auto-generate parameters schema from the run args
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"}
                    }
                }
            }
        }
