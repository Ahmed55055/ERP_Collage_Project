from database.config import DatabaseConfig
from .dto import UserDto
from .IUserRepository import IUserRepository

class UserRepository(IUserRepository):
    """Data access layer for managing user entities in a SQLite database. Handles user creation, retrieval, updates, and deletion operations."""

    def __init__(self, db_config=None):
        """Initializes the repository with a database configuration and creates the users table if it doesn't exist."""
        self.db_config = db_config or DatabaseConfig()
        print(f"Initializing UserRepository with db: {self.db_config.db_name}")  # Added logging
        self._create_table()

    def _create_table(self):
        """Create the users table if it doesn't exist."""
        print("Creating users table")  # Added logging
        self.db_config.execute_query('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')

    def create(self, user_dto):
        """Inserts a new user into the database. Returns True on success, False on failure (e.g., duplicate username/email)."""
        try:
            self.db_config.execute_query('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                                       (user_dto.username, user_dto.email, user_dto.password))
            return True
        except Exception as e:
            print(f"Error creating user {user_dto.username}: {e}")  # Added logging
            # Username or email already exists or other error
            return False

    def get_all(self):
        """Retrieves all users from the database and returns a list of UserDto instances."""
        rows = self.db_config.fetch_all('SELECT username, email, password FROM users')
        return [UserDto(username, email, password) for username, email, password in rows]

    def find_by_username(self, username):
        """Queries the database for a user by username. Returns a UserDto if found, otherwise None."""
        row = self.db_config.fetch_one('SELECT username, email, password FROM users WHERE username = ?', (username,))
        if row:
            return UserDto(row[0], row[1], row[2])
        return None

    def find_by_email(self, email):
        """Queries the database for a user by email. Returns a UserDto if found, otherwise None."""
        row = self.db_config.fetch_one('SELECT username, email, password FROM users WHERE email = ?', (email,))
        if row:
            return UserDto(row[0], row[1], row[2])
        return None

    def exists(self, username):
        """Checks if a user exists by username. Returns True if found, False otherwise."""
        row = self.db_config.fetch_one('SELECT 1 FROM users WHERE username = ?', (username,))
        return row is not None

    def update(self, user_dto):
        """Updates an existing user's email and password by username. Returns True if updated, False otherwise."""
        cursor = self.db_config.execute_query('UPDATE users SET email = ?, password = ? WHERE username = ?',
                                            (user_dto.email, user_dto.password, user_dto.username))
        return cursor.rowcount > 0

    def delete(self, username):
        """Deletes a user by username. Returns True if deleted, False otherwise."""
        cursor = self.db_config.execute_query('DELETE FROM users WHERE username = ?', (username,))
        return cursor.rowcount > 0