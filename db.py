import sqlite3
from datetime import datetime
from typing import Optional, Tuple

def init_db(db_path: str) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            full_name TEXT,
            text TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def log_message(db_path: str, user_id: int, username: str, full_name: str, text: str) -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO messages (user_id, username, full_name, text, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, username, full_name, text, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_stats(db_path: str) -> Tuple[int, int]:
    """returns (total_messages, unique_users)"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM messages")
    total = int(cur.fetchone()[0] or 0)
    cur.execute("SELECT COUNT(DISTINCT user_id) FROM messages")
    users = int(cur.fetchone()[0] or 0)
    conn.close()
    return total, users
