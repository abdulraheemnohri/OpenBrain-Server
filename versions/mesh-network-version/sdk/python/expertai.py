import httpx

class Client:
    def __init__(self, api_key: str, base_url: str = "http://localhost:8000"):
        self.api_key = api_key
        self.base_url = base_url
        self.client = httpx.Client(headers={"x-api-key": self.api_key})

    def chat(self, content: str, model: str = "qwen-3.5-27b", **kwargs):
        """Sends a message to the AI and returns the response."""
        url = f"{self.base_url}/v1/chat/completions"
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": content}],
            **kwargs
        }

        response = self.client.post(url, json=payload)
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"]

    def list_models(self):
        """Returns available models."""
        url = f"{self.base_url}/v1/models"
        response = self.client.get(url)
        response.raise_for_status()
        return response.json()["data"]
