from .db import init_db

def setup_models():
    """Initializes the database schema."""
    init_db()
