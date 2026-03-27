from typing import Dict, Any, Optional
from ..core.ai_engine import get_ai_engine
from ..core.router import get_ai_router
from ..auth.security import validate_api_key, increment_usage

class UACL:
    """Universal AI Connector Layer (UACL) middleware."""
    def __init__(self):
        self.engine = get_ai_engine()
        self.router = get_ai_router()

    async def process_request(self, protocol: str, payload: Dict[str, Any], api_key: Optional[str] = None):
        """Standardizes requests across different protocols (REST, OpenAI, WebSocket, SDK)."""
        # 1. Validation
        if not api_key or not validate_api_key(api_key):
            return {"error": "Unauthorized", "code": 401}

        # 2. Protocol Adaptation (Simplified)
        query = self._extract_query(protocol, payload)
        if not query:
            return {"error": "Invalid payload", "code": 400}

        # 3. Routing & Inference
        # Engine internally handles routing and tool calling now
        result = self.engine.generate_response(query)

        # 4. Usage Tracking
        increment_usage(api_key)

        # 5. Response Adaptation
        return self._format_response(protocol, result, payload)

    def _extract_query(self, protocol: str, payload: Dict[str, Any]) -> str:
        if protocol in ["rest", "openai", "sdk"]:
            if "messages" in payload and len(payload["messages"]) > 0:
                return payload["messages"][-1]["content"]
            elif "prompt" in payload:
                return payload["prompt"]
            elif "query" in payload:
                return payload["query"]
        return ""

    def _format_response(self, protocol: str, result: Dict[str, Any], original_payload: Dict[str, Any]) -> Dict[str, Any]:
        if protocol == "openai":
            # Return OpenAI-compatible response format
            import time
            return {
                "id": f"chatcmpl-{int(time.time())}",
                "object": "chat.completion",
                "created": int(time.time()),
                "model": original_payload.get("model", "expertai-expert"),
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
                    "completion_tokens": result["tokens"],
                    "total_tokens": result["tokens"]
                }
            }
        # Default REST response
        return result

_uacl = None

def get_uacl():
    global _uacl
    if _uacl is None:
        _uacl = UACL()
    return _uacl
