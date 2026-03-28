from ..database.db import get_db_connection
import time

# Simple in-memory cache for rate limiting (reset on restart for now)
rate_limit_cache = {}

def validate_api_key(key: str) -> bool:
    """Checks if the provided API key is valid, active, and within limits."""
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

    # Rate Limiting Logic
    # Get global rate limit from settings
    res = conn.execute("SELECT value FROM settings WHERE key = 'rate_limit'").fetchone()
    global_limit = int(res["value"]) if res else 1000

    current_time = int(time.time() / 60) # Per minute
    limit_key = f"{key}:{current_time}"

    count = rate_limit_cache.get(limit_key, 0)
    if count >= global_limit:
        conn.close()
        print(f"[SECURITY] Rate limit exceeded for key: {key}")
        return False

    rate_limit_cache[limit_key] = count + 1

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
