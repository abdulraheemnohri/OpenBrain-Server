try:
    from llama_cpp import Llama
    LLAMA_CPP_AVAILABLE = True
except ImportError:
    LLAMA_CPP_AVAILABLE = False

# Mapping of task types to GGUF model paths (optimized for Termux)
EXPERT_MODELS = {
    "coding": "models/qwen2.5-coder-3b.gguf",
    "math": "models/qwen2.5-math-1.5b.gguf",
    "reasoning": "models/phi-3-mini-4k.gguf",
    "translation": "models/qwen2.5-1.5b.gguf",
    "general": "models/qwen2.5-3b.gguf"
}

def load_expert_model(expert_name: str):
    """Loads a specific expert model using llama-cpp-python for mobile optimization."""
    if not LLAMA_CPP_AVAILABLE:
        print(f"llama-cpp-python not available, using mock for {expert_name}.")
        return MockLlama(), "cpu"

    model_path = EXPERT_MODELS.get(expert_name, EXPERT_MODELS["general"])
    print(f"Loading mobile-optimized model '{expert_name}' ({model_path}) on CPU/NPU...")

    # Check if model exists, else return mock or error
    import os
    if not os.path.exists(model_path):
        print(f"Model file {model_path} not found, using mock.")
        return MockLlama(), "cpu"

    llm = Llama(model_path=model_path, n_ctx=2048, n_threads=4)
    return llm, "cpu"

class MockLlama:
    def __call__(self, prompt, max_tokens=128, stop=None, echo=False):
        return {
            "choices": [{
                "text": f"Mock mobile response from ExpertAI for: {prompt[:20]}..."
            }]
        }

def load_model():
    # Backwards compatibility for single-model load calls
    return load_expert_model("general")

class MockTokenizer:
    def __call__(self, text, return_tensors=None):
        return {"input_ids": [1, 2, 3]}
    def decode(self, tokens, skip_special_tokens=True):
        return "Mock response from ExpertAI"

class MockModel:
    def generate(self, **kwargs):
        return [[1, 2, 3, 4, 5]]
    def to(self, device):
        return self
