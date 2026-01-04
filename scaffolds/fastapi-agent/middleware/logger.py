from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time
import logging
import json

logger = logging.getLogger("api_tracker")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(message)s'))
logger.addHandler(handler)

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    """
    Middleware to log request latency and status.
    In production, this would send metrics to Datadog/Prometheus/OpenTelemetry.
    """
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Process request
        response = await call_next(request)
        
        process_time = time.time() - start_time
        
        # Log details
        log_data = {
            "path": request.url.path,
            "method": request.method,
            "status_code": response.status_code,
            "latency_ms": round(process_time * 1000, 2)
        }
        
        if request.url.path.startswith("/v1/agent"):
            logger.info(json.dumps(log_data))
            
        return response
