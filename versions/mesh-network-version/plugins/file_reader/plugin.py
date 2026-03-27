import os

def read_local_file(filepath: str):
    """Mocks a file system reader plugin."""
    if os.path.exists(filepath):
        return f"Content of '{filepath}': [File data...]"
    return f"Error: File '{filepath}' not found."

def register_tool():
    """Plugin registration hook."""
    return {
        "name": "file_reader",
        "description": "Reads local files to extract content and information.",
        "func": read_local_file
    }
