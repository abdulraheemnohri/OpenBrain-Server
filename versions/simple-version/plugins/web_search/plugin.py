def search_web(query: str):
    """Mocks a web search plugin."""
    return f"Searching the web for: {query}... [Found news results for 2026]"

def register_tool():
    """Plugin registration hook."""
    return {
        "name": "web_search",
        "description": "Searches the internet for real-time news and information.",
        "func": search_web
    }
