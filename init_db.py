# init_db.py
import sqlite3
import os

DB_PATH = r"D:/Uni/Hackathon/SIH/SIH Project/greenlight.db"   # same everywhere
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp INTEGER,
    vehicle_count INTEGER,
    action TEXT,
    duration INTEGER
)
""")

conn.commit()
conn.close()

print("Database and table created successfully at:", DB_PATH)