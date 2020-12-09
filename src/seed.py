import sqlite3

db = sqlite3.connect("warp.db")
cursor = db.cursor()

names = """CREATE TABLE IF NOT EXISTS warp_points (
         name TEXT NOT NULL UNIQUE,
         path TEXT NOT NULL UNIQUE 
);"""

cursor.execute(names)
