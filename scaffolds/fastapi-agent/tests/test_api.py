from fastapi.testclient import TestClient
from main import app
from services.llm import LLMService

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

class MockLLMService:
    async def get_response(self, prompt: str, system_prompt: str = "") -> str:
        return "Mocked response"

# Patch the LLM service for testing
app.dependency_overrides = {} 
# Note: Since the service is instantiated globally in main.py, 
# deeper mocking would require headers or dependency injection refactoring.
# For this simple scaffold, we'll test valid input flow assuming credentials might fail or be mocked differently.
# But actually, let's just test the health endpoint and validation for now to avoid complexity without a full DI container.

def test_run_agent_validation_error():
    # Missing query
    response = client.post("/v1/agent/run", json={})
    assert response.status_code == 422
