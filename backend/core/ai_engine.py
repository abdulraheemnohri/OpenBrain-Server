import time
from .model_loader import load_expert_model, TORCH_AVAILABLE
from .router import get_ai_router

class AIEngine:
    def __init__(self):
        # Cache for experts to prevent re-loading if they're already loaded
        # In a very resource-constrained environment, we'd unload them when not in use.
        self.experts = {}
        self.router = get_ai_router()
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

        tokenizer, model, device = self.experts[task_type]

        # Mock logic
        if not TORCH_AVAILABLE:
            response_text = f"[{task_type.upper()} EXPERT] Mock response for: {query}"
            time.sleep(0.5)
            return {
                "response": response_text,
                "tokens": 20,
                "response_time": 0.5
            }

        # Inference logic
        import torch
        inputs = tokenizer(query, return_tensors="pt")
        for k in inputs:
            inputs[k] = inputs[k].to(device)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=0.7,
                do_sample=True,
                top_p=0.9
            )

        response_text = tokenizer.decode(output[0], skip_special_tokens=True)
        # Robust response cleaning: remove prompt if it's mirrored
        if response_text.startswith(query):
            response_text = response_text[len(query):].strip()

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
