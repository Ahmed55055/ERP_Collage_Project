from database.config import DatabaseConfig
from .dto import ItemDto
from .IStorageRepository import IStorageRepository

class StorageRepository(IStorageRepository):
    """Data access layer for managing items in a SQLite database. Uses a DatabaseConfig instance for database operations and interacts with ItemDto objects for data transfer. Handles CRUD operations for items with fields: id, name, quantity, and price."""

    def __init__(self, db_config=None):
        """Initializes the repository, sets the database config, and creates the items table if it doesn't exist."""
        self.db_config = db_config or DatabaseConfig()
        self._create_table()

    def _create_table(self):
        """Create the items table if it doesn't exist."""
        self.db_config.execute_query('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                quantity INTEGER,
                price REAL
            )
        ''')

    def create(self, item_dto):
        """Inserts a new item into the database. Returns True on success, False on failure (e.g., duplicate name)."""
        try:
            self.db_config.execute_query('INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)',
                                       (item_dto.name, item_dto.quantity, item_dto.price))
            return True
        except Exception:
            # Name already exists or other error
            return False

    def get_all(self):
        """Retrieves all items from the database and returns a list of ItemDto instances."""
        rows = self.db_config.fetch_all('SELECT name, quantity, price FROM items')
        return [ItemDto(name, quantity, price) for name, quantity, price in rows]

    def find_by_name(self, name):
        """Queries the database for an item by name. Returns an ItemDto if found, otherwise None."""
        row = self.db_config.fetch_one('SELECT name, quantity, price FROM items WHERE name = ?', (name,))
        if row:
            return ItemDto(row[0], row[1], row[2])
        return None

    def exists(self, name):
        """Checks for the existence of an item by name. Returns True if found, False otherwise."""
        row = self.db_config.fetch_one('SELECT 1 FROM items WHERE name = ?', (name,))
        return row is not None

    def update(self, item_dto):
        """Updates an existing item's quantity and price by name. Returns True if updated, False otherwise."""
        cursor = self.db_config.execute_query('UPDATE items SET quantity = ?, price = ? WHERE name = ?',
                                            (item_dto.quantity, item_dto.price, item_dto.name))
        return cursor.rowcount > 0

    def delete(self, name):
        """Deletes an item by name. Returns True if deleted, False otherwise."""
        cursor = self.db_config.execute_query('DELETE FROM items WHERE name = ?', (name,))
        return cursor.rowcount > 0