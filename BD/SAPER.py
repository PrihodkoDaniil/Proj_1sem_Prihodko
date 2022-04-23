import sqlite3 as sq
info_users=[
    (1, 'Алексей',1, 22, 1000),
    (2, 'Максим',1, 36, 5000),
    (3, 'Алиса',2, 18, 900),
    (4, 'Михаель',1, 24, 1050),
    (5, 'Юлианна',2, 16, 600),
]
with sq.connect('SAPER.db') as con:
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex INTEGER NOT NULL DEFAULT 1,
            old INTEGER,
            score INTGER
            )""")
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)