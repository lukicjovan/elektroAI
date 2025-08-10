import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "app.db")

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projekti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sheme (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER,
        file_path TEXT,
        preview_path TEXT,
        FOREIGN KEY(project_id) REFERENCES projekti(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS korisnicka_aktivnost (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        event_type TEXT,
        metadata TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        rating INTEGER,
        comment TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ui_varijante (
        user_id TEXT PRIMARY KEY,
        variant TEXT
    )
    """)

    conn.commit()
    conn.close()

def get_projects():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM projekti")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]

def insert_shema(project_id, file_path, preview_path):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sheme (project_id, file_path, preview_path) VALUES (?, ?, ?)",
                   (project_id, file_path, preview_path))
    conn.commit()
    conn.close()