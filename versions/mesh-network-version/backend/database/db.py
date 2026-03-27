import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "openbrain.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open(os.path.join(os.path.dirname(__file__), "models.sql"), "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
