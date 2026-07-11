"""
==============================================================================
Database

Purpose
-------
Lightweight SQLite store for user accounts and OTP verification
sessions - kept separate from the Excel-based enterprise datasets,
since this is transactional account data rather than analytics data.

Author
------
Sandipan Choudhury
==============================================================================
"""

import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DB_DIR = PROJECT_ROOT / "database"

DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "app.db"


class Database:

    def __init__(self):

        self._init_schema()

    def get_connection(self):

        connection = sqlite3.connect(DB_PATH)

        connection.row_factory = sqlite3.Row

        connection.execute("PRAGMA foreign_keys = ON")

        return connection

    def _init_schema(self):

        connection = self.get_connection()

        connection.execute("""

            CREATE TABLE IF NOT EXISTS users (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                full_name TEXT NOT NULL,

                username TEXT UNIQUE NOT NULL,

                email TEXT UNIQUE NOT NULL,

                phone TEXT UNIQUE NOT NULL,

                password_hash TEXT NOT NULL,

                is_verified INTEGER NOT NULL DEFAULT 0,

                last_login TEXT,

                created_at TEXT NOT NULL

            )

        """)

        # Migration: add last_login to any users table that was
        # created before this column existed.

        try:

            connection.execute(

                "ALTER TABLE users ADD COLUMN last_login TEXT"

            )

        except sqlite3.OperationalError:

            pass

        connection.execute("""

            CREATE TABLE IF NOT EXISTS otp_sessions (

                id TEXT PRIMARY KEY,

                user_id INTEGER NOT NULL,

                purpose TEXT NOT NULL,

                otp_code_hash TEXT NOT NULL,

                attempts INTEGER NOT NULL DEFAULT 0,

                expires_at TEXT NOT NULL,

                verified INTEGER NOT NULL DEFAULT 0,

                pending_value TEXT,

                created_at TEXT NOT NULL,

                FOREIGN KEY(user_id) REFERENCES users(id)

            )

        """)

        # Migration: add pending_value to any otp_sessions table that
        # was created before this column existed.

        try:

            connection.execute(

                "ALTER TABLE otp_sessions ADD COLUMN pending_value TEXT"

            )

        except sqlite3.OperationalError:

            pass

        connection.commit()

        connection.close()


database = Database()
