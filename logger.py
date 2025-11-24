# logger.py
import sqlite3
import time

DB = "greenlight.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            vehicle_count INTEGER,
            action TEXT,
            duration INTEGER
        )
    """)
    conn.commit()
    conn.close()

def log_event(vehicle_count, action, duration):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        INSERT INTO logs(timestamp, vehicle_count, action, duration)
        VALUES(?,?,?,?)
    """, (int(time.time()), vehicle_count, action, duration))
    conn.commit()
    conn.close()