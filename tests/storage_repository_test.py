import unittest
import os
from storage.StorageRepository import StorageRepository
from storage.dto import ItemDto
from database.config import DatabaseConfig

class TestStorageRepository(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_db = 'test_storage_repo.db'
        self.db_config = DatabaseConfig(self.test_db)
        self.repo = StorageRepository(self.db_config)
        # Clear the table to ensure clean state for each test
        self.db_config.execute_query('DELETE FROM items')

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        # Close any open connections first
        try:
            if hasattr(self, 'db_config'):
                # Force close any connections
                pass
        except:
            pass
        # Wait a bit for connections to close
        import time
        time.sleep(0.1)
        if os.path.exists(self.test_db):
            try:
                os.remove(self.test_db)
            except PermissionError:
                # If still locked, skip for now
                pass

    def test_create_item(self):
        """Test creating a new item."""
        item = ItemDto("Apple", 10, 1.50)
        result = self.repo.create(item)
        self.assertTrue(result)

        # Verify item was created
        found_item = self.repo.find_by_name("Apple")
        self.assertIsNotNone(found_item)
        self.assertEqual(found_item.name, "Apple")
        self.assertEqual(found_item.quantity, 10)
        self.assertEqual(found_item.price, 1.50)

    def test_create_duplicate_item(self):
        """Test creating an item with duplicate name fails."""
        item1 = ItemDto("Apple", 10, 1.50)
        item2 = ItemDto("Apple", 20, 2.00)

        result1 = self.repo.create(item1)
        result2 = self.repo.create(item2)

        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_get_all_items(self):
        """Test retrieving all items."""
        # Create test items
        self.repo.create(ItemDto("Apple", 10, 1.50))
        self.repo.create(ItemDto("Banana", 20, 0.75))

        items = self.repo.get_all()
        self.assertEqual(len(items), 2)

        # Check items are returned as DTOs
        item_names = [item.name for item in items]
        self.assertIn("Apple", item_names)
        self.assertIn("Banana", item_names)

    def test_find_by_name_existing(self):
        """Test finding an existing item by name."""
        self.repo.create(ItemDto("Orange", 15, 2.00))

        item = self.repo.find_by_name("Orange")
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Orange")
        self.assertEqual(item.quantity, 15)
        self.assertEqual(item.price, 2.00)

    def test_find_by_name_nonexistent(self):
        """Test finding a nonexistent item by name."""
        item = self.repo.find_by_name("Nonexistent")
        self.assertIsNone(item)

    def test_exists_true(self):
        """Test exists method returns True for existing item."""
        self.repo.create(ItemDto("Grape", 5, 3.00))
        self.assertTrue(self.repo.exists("Grape"))

    def test_exists_false(self):
        """Test exists method returns False for nonexistent item."""
        self.assertFalse(self.repo.exists("Nonexistent"))

    def test_update_existing_item(self):
        """Test updating an existing item."""
        # Create initial item
        self.repo.create(ItemDto("Apple", 10, 1.50))

        # Update item
        updated_item = ItemDto("Apple", 25, 1.75)
        result = self.repo.update(updated_item)
        self.assertTrue(result)

        # Verify update
        found_item = self.repo.find_by_name("Apple")
        self.assertEqual(found_item.quantity, 25)
        self.assertEqual(found_item.price, 1.75)

    def test_update_nonexistent_item(self):
        """Test updating a nonexistent item."""
        updated_item = ItemDto("Nonexistent", 25, 1.75)
        result = self.repo.update(updated_item)
        self.assertFalse(result)

    def test_delete_existing_item(self):
        """Test deleting an existing item."""
        self.repo.create(ItemDto("Apple", 10, 1.50))

        result = self.repo.delete("Apple")
        self.assertTrue(result)

        # Verify deletion
        self.assertFalse(self.repo.exists("Apple"))

    def test_delete_nonexistent_item(self):
        """Test deleting a nonexistent item."""
        result = self.repo.delete("Nonexistent")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()