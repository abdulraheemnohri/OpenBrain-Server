from ..database.db import get_db_connection

def get_daily_metrics(limit: int = 30):
    """Retrieves daily metrics for analytics visualization."""
    conn = get_db_connection()
    metrics = conn.execute("SELECT * FROM metrics ORDER BY date DESC LIMIT ?", (limit,)).fetchall()
    conn.close()
    return [dict(m) for m in metrics]

def get_total_usage_stats():
    """Retrieves total usage stats across all time."""
    conn = get_db_connection()
    stats = conn.execute(
        "SELECT SUM(total_requests) as total_requests, SUM(total_tokens) as total_tokens, AVG(avg_response_time) as avg_response_time FROM metrics"
    ).fetchone()
    conn.close()
    return dict(stats)
