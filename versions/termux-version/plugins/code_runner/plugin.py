def execute_code(code: str):
    """Mocks a code runner plugin."""
    return f"Executing code: [Output: Success] - Code was: {code[:30]}..."

def register_tool():
    """Plugin registration hook."""
    return {
        "name": "code_runner",
        "description": "Safely executes code snippets and returns the output.",
        "func": execute_code
    }
