import sqlite3
from database import DB_PATH

def track_event(feature_name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usage (
            feature TEXT,
            count INTEGER
        )
    """)
    cursor.execute("""
        SELECT count FROM usage WHERE feature = ?
    """, (feature_name,))
    result = cursor.fetchone()

    if result:
        cursor.execute("""
            UPDATE usage SET count = count + 1 WHERE feature = ?
        """, (feature_name,))
    else:
        cursor.execute("""
            INSERT INTO usage (feature, count) VALUES (?, 1)
        """, (feature_name,))
    conn.commit()
    conn.close()

def get_top_features(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT feature, count FROM usage ORDER BY count DESC LIMIT ?
    """, (limit,))
    top_features = cursor.fetchall()
    conn.close()
    return top_features