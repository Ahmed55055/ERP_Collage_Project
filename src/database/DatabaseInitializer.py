from .IDatabase import IDatabase

class DatabaseInitializer:
    def __init__(self, database: IDatabase):
        self.database = database

    def initialize_storage_schema(self):
        """Initialize the schema for storage items."""
        self.database.execute_query('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                quantity INTEGER,
                price REAL
            )
        ''')

    def initialize_user_schema(self):
        """Initialize the schema for users."""
        self.database.execute_query('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')