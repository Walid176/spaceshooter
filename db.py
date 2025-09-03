import sqlite3
conn = sqlite3.connect("game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS highscores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER)
""")
conn.commit()

def add_score(name, score):
    cursor.execute("INSERT INTO highscores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()

def get_highscores(limit = 10):
    cursor.execute("SELECT name, score FROM highscores ORDER BY score DESC LIMIT ?", (limit,))
    return cursor.fetchall()



def delete_score():
    cursor.execute("DELETE FROM highscores")
    conn.commit()
    