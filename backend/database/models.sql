CREATE TABLE IF NOT EXISTS api_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL UNIQUE,
    status TEXT NOT NULL DEFAULT 'active', -- active, disabled
    usage_limit INTEGER,
    usage_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    api_key TEXT,
    query TEXT,
    response TEXT,
    tokens INTEGER,
    response_time REAL,
    ip_address TEXT,
    FOREIGN KEY (api_key) REFERENCES api_keys(key)
);

CREATE TABLE IF NOT EXISTS metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE DEFAULT CURRENT_DATE,
    total_requests INTEGER DEFAULT 0,
    total_tokens INTEGER DEFAULT 0,
    avg_response_time REAL DEFAULT 0,
    UNIQUE(date)
);
