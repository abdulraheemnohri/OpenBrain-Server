try:
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False

# Mapping of task types to expert models (simplified for demonstration)
# In reality, these might be smaller versions of Qwen or different models like Phi-3
EXPERT_MODELS = {
    "coding": "Qwen/Qwen2.5-Coder-3B-Instruct-GPTQ-Int4",
    "math": "Qwen/Qwen2.5-Math-1.5B-Instruct-GPTQ-Int4",
    "general": "Qwen/Qwen2.5-3B-Instruct-GPTQ-Int4"
}

def load_expert_model(expert_name: str):
    """Loads a specific expert model with GPU/CPU fallback."""
    if not TORCH_AVAILABLE:
        print(f"Torch/Transformers not available, using mock for {expert_name}.")
        return MockTokenizer(), MockModel(), "cpu"

    model_id = EXPERT_MODELS.get(expert_name, EXPERT_MODELS["general"])
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading expert model '{expert_name}' ({model_id}) on {device}...")

    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        trust_remote_code=True
    )

    return tokenizer, model, device

class MockTokenizer:
    def __call__(self, text, return_tensors=None):
        return {"input_ids": [1, 2, 3]}
    def decode(self, tokens, skip_special_tokens=True):
        return "Mock response from OpenBrain"

class MockModel:
    def generate(self, **kwargs):
        return [[1, 2, 3, 4, 5]]
    def to(self, device):
        return self
