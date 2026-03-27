import secrets
from ..database.db import get_db_connection

def generate_api_key(usage_limit: int = 1000):
    """Generates a new API key."""
    key = "sk-" + secrets.token_hex(20)

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO api_keys (key, usage_limit) VALUES (?, ?)",
        (key, usage_limit)
    )
    conn.commit()
    conn.close()

    return key

def disable_api_key(key: str):
    """Disables an existing API key."""
    conn = get_db_connection()
    conn.execute(
        "UPDATE api_keys SET status = 'disabled' WHERE key = ?",
        (key,)
    )
    conn.commit()
    conn.close()

def delete_api_key(key: str):
    """Deletes an API key."""
    conn = get_db_connection()
    conn.execute("DELETE FROM api_keys WHERE key = ?", (key,))
    conn.commit()
    conn.close()

def get_all_api_keys():
    """Returns all API keys in the system."""
    conn = get_db_connection()
    keys = conn.execute("SELECT * FROM api_keys").fetchall()
    conn.close()
    return [dict(k) for k in keys]
