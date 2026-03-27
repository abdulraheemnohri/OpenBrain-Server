from ..database.db import get_db_connection

def validate_api_key(key: str) -> bool:
    """Checks if the provided API key is valid and has usage remaining."""
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM api_keys WHERE key = ? AND status = 'active'",
        (key,)
    ).fetchone()

    if not row:
        conn.close()
        return False

    usage_limit = row["usage_limit"]
    usage_count = row["usage_count"]

    if usage_limit is not None and usage_count >= usage_limit:
        conn.close()
        return False

    conn.close()
    return True

def increment_usage(key: str):
    """Increments the usage count for a given API key."""
    conn = get_db_connection()
    conn.execute(
        "UPDATE api_keys SET usage_count = usage_count + 1 WHERE key = ?",
        (key,)
    )
    conn.commit()
    conn.close()
