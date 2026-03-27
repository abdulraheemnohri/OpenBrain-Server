from ..database.db import get_db_connection

def log_request(api_key: str, query: str, response: str, tokens: int, response_time: float, ip_address: str):
    """Logs the request into the database."""
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO logs (api_key, query, response, tokens, response_time, ip_address) VALUES (?, ?, ?, ?, ?, ?)",
        (api_key, query, response, tokens, response_time, ip_address)
    )

    # Update metrics for analytics
    conn.execute(
        """
        INSERT INTO metrics (date, total_requests, total_tokens, avg_response_time)
        VALUES (CURRENT_DATE, 1, ?, ?)
        ON CONFLICT(date) DO UPDATE SET
            total_requests = total_requests + 1,
            total_tokens = total_tokens + EXCLUDED.total_tokens,
            avg_response_time = (avg_response_time * (total_requests - 1) + EXCLUDED.avg_response_time) / total_requests
        """,
        (tokens, response_time)
    )

    conn.commit()
    conn.close()

def get_recent_logs(limit: int = 100):
    """Retrieves recent logs for the dashboard."""
    conn = get_db_connection()
    logs = conn.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT ?", (limit,)).fetchall()
    conn.close()
    return [dict(l) for l in logs]
