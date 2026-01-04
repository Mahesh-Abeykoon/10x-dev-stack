from openai import AsyncOpenAI
from typing import AsyncGenerator
from config import get_settings

settings = get_settings()

class LLMService:
    """
    Unified interface for LLM providers (OpenAI, Anthropic, etc).
    Currently implemented for OpenAI.
    """
    def __init__(self):
        # Initialize client only if key is present
        self.client = None
        if settings.OPENAI_API_KEY:
            self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def get_response(self, prompt: str, system_prompt: str = "You are a helpful AI assistant.") -> str:
        """
        Get a simple string response from the LLM.
        """
        if not self.client:
            return "Error: OPENAI_API_KEY not configured."

        completion = await self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    async def stream_response(self, prompt: str, system_prompt: str = "You are a helpful AI assistant.") -> AsyncGenerator[str, None]:
        """
        Stream the response purely as text chunks.
        """
        if not self.client:
            yield "Error: OPENAI_API_KEY not configured."
            return

        stream = await self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
