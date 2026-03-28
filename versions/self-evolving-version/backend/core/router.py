import re

class AIRouter:
    def __init__(self):
        self.experts = {
            "coding": ["python", "javascript", "code", "function", "class", "script", "api", "html", "css", "program", "developer"],
            "math": ["calculate", "solve", "math", "integral", "derivative", "sum", "multiplication", "equation", "formula", "algebra"],
            "reasoning": ["think", "reason", "step by step", "complex", "analyze", "explain", "why", "logic", "strategy"],
            "translation": ["translate", "language", "english", "hindi", "spanish", "french", "german", "chinese", "write in"],
            "general": []
        }

    def route_query(self, query: str) -> str:
        """Determines the task type/expert for the given query."""
        query_lower = query.lower()

        for expert, keywords in self.experts.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', query_lower):
                    return expert

        return "general"

_router = None

def get_ai_router():
    global _router
    if _router is None:
        _router = AIRouter()
    return _router
