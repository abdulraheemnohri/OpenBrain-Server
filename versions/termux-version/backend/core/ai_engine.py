import time
from .model_loader import load_expert_model, LLAMA_CPP_AVAILABLE
from .router import get_ai_router
from ..tools.tool_manager import get_tool_manager

class AIEngine:
    def __init__(self):
        # Cache for experts to prevent re-loading if they're already loaded
        # In a very resource-constrained environment, we'd unload them when not in use.
        self.experts = {}
        self.router = get_ai_router()
        self.tool_manager = get_tool_manager()
        self.current_expert = None

    def generate_response(self, query: str, max_tokens: int = 512) -> dict:
        """Determines the correct expert, loads it if necessary, and generates a response."""
        start_time = time.time()

        # Route query
        task_type = self.router.route_query(query)
        print(f"Routing query to '{task_type}' expert...")

        # Expert Loading (Lazy Load)
        if task_type not in self.experts:
            # Unload current expert to save memory? Let's implement a simple single-expert mode for now.
            if self.experts and len(self.experts) >= 1:
                # Keep only 1 expert at a time in memory to maximize device support
                # Note: In a real system, you'd use del expert and torch.cuda.empty_cache()
                print("Unloading previous expert to free up resources...")
                self.experts.clear()

            self.experts[task_type] = load_expert_model(task_type)

        llm, device = self.experts[task_type]

        # Inference logic (Mobile Optimized)
        if not LLAMA_CPP_AVAILABLE or (hasattr(llm, "__class__") and llm.__class__.__name__ == "MockLlama"):
            response_text = f"[{task_type.upper()} MOBILE EXPERT] Mock response for: {query}"
            time.sleep(0.5)
            token_count = 20
        else:
            # Real llama-cpp-python inference
            output = llm(
                f"User: {query}\nAssistant:",
                max_tokens=max_tokens,
                stop=["User:", "\n"],
                echo=False
            )
            response_text = output["choices"][0]["text"].strip()
            token_count = output.get("usage", {}).get("completion_tokens", 20)
        # Robust response cleaning: remove prompt if it's mirrored
        if response_text.startswith(query):
            response_text = response_text[len(query):].strip()

        # Tool detection and execution logic (Mock)
        if "search" in query.lower() and "web_search" in self.tool_manager.tools:
            tool_result = self.tool_manager.execute_tool("web_search", query)
            response_text += f"\n\n[TOOL EXECUTION]: {tool_result}"
        elif "read" in query.lower() and "file_reader" in self.tool_manager.tools:
            # Attempt to extract path if exists or use query
            tool_result = self.tool_manager.execute_tool("file_reader", "config.txt")
            response_text += f"\n\n[TOOL EXECUTION]: {tool_result}"

        end_time = time.time()
        response_time = end_time - start_time
        token_count = len(output[0])

        return {
            "response": response_text,
            "tokens": token_count,
            "response_time": response_time
        }

_engine = None

def get_ai_engine():
    global _engine
    if _engine is None:
        _engine = AIEngine()
    return _engine
