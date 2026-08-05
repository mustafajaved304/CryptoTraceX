import sqlite3
import os

DB_PATH = "database/cryptotracex.db"


class Database:

    def __init__(self):
        os.makedirs("database", exist_ok=True)
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            sha256 TEXT,
            bitcoin TEXT,
            ethereum TEXT,
            urls TEXT,
            ips TEXT,
            emails TEXT,
            risk TEXT,
            analysis_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS wallets(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wallet TEXT,
            blockchain TEXT,
            balance TEXT,
            transactions INTEGER,
            risk TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.conn.commit()

    def save_analysis(self, data):

        self.cursor.execute("""
        INSERT INTO analysis
        (
        filename,
        sha256,
        bitcoin,
        ethereum,
        urls,
        ips,
        emails,
        risk
        )

        VALUES(?,?,?,?,?,?,?,?)

        """,

        (

        data["filename"],
        data["sha256"],
        ", ".join(data["bitcoin"]),
        ", ".join(data["ethereum"]),
        ", ".join(data["urls"]),
        ", ".join(data["ips"]),
        ", ".join(data["emails"]),
        data["risk"]

        )

        )

        self.conn.commit()

    def save_wallet(self,
                    wallet,
                    blockchain,
                    balance,
                    transactions,
                    risk):

        self.cursor.execute("""

        INSERT INTO wallets

        (

        wallet,
        blockchain,
        balance,
        transactions,
        risk

        )

        VALUES(?,?,?,?,?)

        """,

        (

        wallet,
        blockchain,
        balance,
        transactions,
        risk

        )

        )

        self.conn.commit()

    def get_analysis(self):

        self.cursor.execute("""

        SELECT *

        FROM analysis

        ORDER BY id DESC

        """)

        return self.cursor.fetchall()

    def get_wallets(self):

        self.cursor.execute("""

        SELECT *

        FROM wallets

        ORDER BY id DESC

        """)

        return self.cursor.fetchall()


db = Database()


if __name__ == "__main__":

    print("Database Ready ✅")