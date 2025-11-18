import sqlite3
from .IDatabase import IDatabase

class SQLiteDatabase(IDatabase):
    def __init__(self, db_name='storage.db'):
        self.db_name = db_name
        self.conn = None
        if db_name == ':memory:':
            self.conn = sqlite3.connect(':memory:')

    def get_connection(self):
        """Get a database connection."""
        if self.conn:
            return self.conn
        return sqlite3.connect(self.db_name)

    def execute_query(self, query, params=None):
        """Execute a query with optional parameters."""
        if self.db_name == ':memory:':
            conn = self.get_connection()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor
        else:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                return cursor

    def fetch_one(self, query, params=None):
        """Fetch one row from the database."""
        if self.db_name == ':memory:':
            conn = self.get_connection()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()
        else:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchone()

    def fetch_all(self, query, params=None):
        """Fetch all rows from the database."""
        if self.db_name == ':memory:':
            conn = self.get_connection()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        else:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()