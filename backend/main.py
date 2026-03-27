import time
from fastapi import FastAPI, Request, HTTPException, Header, Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional
from pydantic import BaseModel
import os

from .database.models import setup_models
from .auth.security import validate_api_key, increment_usage
from .auth.api_keys import generate_api_key, disable_api_key, delete_api_key, get_all_api_keys
from .logs.logger import log_request, get_recent_logs
from .analytics.metrics import get_daily_metrics, get_total_usage_stats
from .core.ai_engine import get_ai_engine
from .core.router import get_ai_router

app = FastAPI(title="OpenBrain Server")

# Initialize database
setup_models()

# Static files & Templates (dashboard)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="dashboard")

# Models for request bodies
class ChatCompletionRequest(BaseModel):
    model: str = "qwen-3.5-27b"
    messages: List[dict]
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.7

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/apikeys")
async def apikeys_page(request: Request):
    return templates.TemplateResponse(request=request, name="apikeys.html")

@app.get("/logs")
async def logs_page(request: Request):
    return templates.TemplateResponse(request=request, name="logs.html")

@app.get("/analytics")
async def analytics_page(request: Request):
    return templates.TemplateResponse(request=request, name="analytics.html")

@app.get("/settings")
async def settings_page(request: Request):
    return templates.TemplateResponse(request=request, name="settings.html")

# OpenAI-compatible Chat Completions endpoint
@app.post("/v1/chat/completions")
async def chat_completions(
    request: Request,
    body: ChatCompletionRequest,
    x_api_key: Optional[str] = Header(None)
):
    if not x_api_key or not validate_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid API Key")

    query = body.messages[-1]["content"]

    # Optional Routing
    router = get_ai_router()
    task_type = router.route_query(query)

    # Inference
    engine = get_ai_engine()
    result = engine.generate_response(query, max_tokens=body.max_tokens)

    # Logging
    log_request(
        api_key=x_api_key,
        query=query,
        response=result["response"],
        tokens=result["tokens"],
        response_time=result["response_time"],
        ip_address=request.client.host
    )

    # Increment usage
    increment_usage(x_api_key)

    return {
        "id": f"chatcmpl-{int(time.time())}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": body.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": result["response"]
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 0, # Simplified
            "completion_tokens": result["tokens"],
            "total_tokens": result["tokens"]
        }
    }

@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "qwen-3.5-27b",
                "object": "model",
                "created": 1677610602,
                "owned_by": "openbrain"
            }
        ]
    }

# Admin API Endpoints
@app.get("/api/admin/keys")
async def admin_get_keys():
    return get_all_api_keys()

@app.post("/api/admin/keys")
async def admin_create_key(usage_limit: int = 1000):
    key = generate_api_key(usage_limit)
    return {"key": key}

@app.delete("/api/admin/keys/{key}")
async def admin_delete_key(key: str):
    delete_api_key(key)
    return {"status": "success"}

@app.get("/api/admin/logs")
async def admin_get_logs(limit: int = 100):
    return get_recent_logs(limit)

@app.get("/api/admin/analytics")
async def admin_get_analytics():
    return {
        "daily": get_daily_metrics(),
        "total": get_total_usage_stats()
    }

@app.get("/api/admin/tools")
async def admin_get_tools():
    from .tools.tool_manager import get_tool_manager
    return get_tool_manager().get_available_tools()
