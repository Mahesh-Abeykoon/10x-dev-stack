from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from config import get_settings

settings = get_settings()

class SecurityMiddleware(BaseHTTPMiddleware):
    """
    Simple API Key Authentication.
    Clients must send 'X-API-Key: <secret>' header.
    """
    async def dispatch(self, request: Request, call_next):
        # Allow health check without auth
        if request.url.path in ["/health", "/docs", "/openapi.json"]:
            return await call_next(request)
            
        api_key = request.headers.get("X-API-Key")
        
        if api_key != settings.API_SECRET:
            return JSONResponse(
                status_code=401,
                content={"detail": "Invalid or missing API Key"}
            )
            
        return await call_next(request)
