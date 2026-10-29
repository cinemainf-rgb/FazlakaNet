import sqlite3

class Database:

    def __init__(self):

        self.conn = sqlite3.connect(
            "sales.db"
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY,
            code TEXT,
            profile TEXT
        )
        """)

        self.conn.commit()

    def add_sale(
        self,
        code,
        profile
    ):

        self.cur.execute(
        """
        INSERT INTO sales(
            code,
            profile
        )
        VALUES(
            ?,
            ?
        )
        """,
        (
        code,
        profile
        ))

        self.conn.commit()
