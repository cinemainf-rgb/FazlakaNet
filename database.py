import sqlite3

class Database:

    def __init__(self):

        self.conn = sqlite3.connect(
            "sales.db",
            check_same_thread=False
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            profile TEXT,
            sale_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def add_sale(
        self,
        code,
        profile
    ):

        self.cur.execute(
            '''
            INSERT INTO sales
            (
            code,
            profile
            )
            VALUES
            (
            ?,
            ?
            )
            ''',
            (
                code,
                profile
            )
        )

        self.conn.commit()

    def get_total_sales(self):

        self.cur.execute(
            "SELECT COUNT(*) FROM sales"
        )

        return self.cur.fetchone()[0]

    def get_last_sale(self):

        self.cur.execute(
            """
            SELECT code
            FROM sales
            ORDER BY id DESC
            LIMIT 1
            """
        )

        return self.cur.fetchone()
