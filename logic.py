import sqlite3


class TaskManager:
    def __init__(self, database):
        self.database = database
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                user_id INTEGER
            )
            """)
            conn.commit()

    def add_task(self, user_id, name, description):
        con = sqlite3.connect(self.database)
        with con:
            con.execute("INSERT INTO tasks (user_id, name, description) VALUES(?, ?, ?)",
                        (user_id, name, description))
            con.commit()

    def delete_task(self, name):
        con = sqlite3.connect(self.database)
        with con:
            con.execute("DELETE FROM tasks WHERE name = ?", (name,))
            con.commit()

    def select_task(self, user_id):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT name FROM tasks WHERE user_id = ?", (user_id,))
            return cur.fetchall()
