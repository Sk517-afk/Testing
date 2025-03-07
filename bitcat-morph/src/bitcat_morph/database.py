import sqlite3

def listScores():
    conn = sqlite3.connect("db.db")
    cur = conn.cursor()

    result = cur.execute("SELECT * FROM 'scores'")

    print(result.fetchall())