import sqlite3

DB_PATH = "data/user_data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_progress 
                 (user_id TEXT, xp INTEGER, streak INTEGER)''')
    conn.commit()
    conn.close()

def update_xp(user_id, xp_gained):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT xp, streak FROM user_progress WHERE user_id=?", (user_id,))
    data = c.fetchone()
    if data:
        new_xp = data[0] + xp_gained
        new_streak = data[1] + 1
        c.execute("UPDATE user_progress SET xp=?, streak=? WHERE user_id=?", (new_xp, new_streak, user_id))
    else:
        c.execute("INSERT INTO user_progress VALUES (?, ?, ?)", (user_id, xp_gained, 1))
    conn.commit()
    conn.close()
