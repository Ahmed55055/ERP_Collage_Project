import unittest
from unittest.mock import Mock
from ..src.storage.Repository.StorageRepository import StorageRepository
from ..src.storage.dto import ItemDto

class TestStorageRepository(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.db_config = Mock()
        self.repo = StorageRepository(self.db_config)
        self.db_config.reset_mock()

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        pass

    def test_create_item(self):
        """Test creating a new item."""
        item = ItemDto("Apple", 10, 1.50)
        result = self.repo.create(item)
        self.assertTrue(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)',
            ("Apple", 10, 1.50)
        )

    def test_create_duplicate_item(self):
        """Test creating an item with duplicate name fails."""
        item1 = ItemDto("Apple", 10, 1.50)
        item2 = ItemDto("Apple", 20, 2.00)

        # First create succeeds
        result1 = self.repo.create(item1)
        self.assertTrue(result1)

        # Mock second create to raise exception (duplicate)
        self.db_config.execute_query.side_effect = Exception("Duplicate")

        result2 = self.repo.create(item2)
        self.assertFalse(result2)

        # Verify calls
        self.assertEqual(self.db_config.execute_query.call_count, 2)

    def test_get_all_items(self):
        """Test retrieving all items."""
        # Mock fetch_all to return test data
        self.db_config.fetch_all.return_value = [
            ("Apple", 10, 1.50),
            ("Banana", 20, 0.75)
        ]

        items = self.repo.get_all()
        self.assertEqual(len(items), 2)

        # Check items are returned as DTOs
        item_names = [item.name for item in items]
        self.assertIn("Apple", item_names)
        self.assertIn("Banana", item_names)

        # Verify fetch_all was called
        self.db_config.fetch_all.assert_called_once_with('SELECT name, quantity, price FROM items')

    def test_find_by_name_existing(self):
        """Test finding an existing item by name."""
        # Mock fetch_one to return data
        self.db_config.fetch_one.return_value = ("Orange", 15, 2.00)

        item = self.repo.find_by_name("Orange")
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Orange")
        self.assertEqual(item.quantity, 15)
        self.assertEqual(item.price, 2.00)

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT name, quantity, price FROM items WHERE name = ?', ("Orange",))

    def test_find_by_name_nonexistent(self):
        """Test finding a nonexistent item by name."""
        # Mock fetch_one to return None
        self.db_config.fetch_one.return_value = None

        item = self.repo.find_by_name("Nonexistent")
        self.assertIsNone(item)

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT name, quantity, price FROM items WHERE name = ?', ("Nonexistent",))

    def test_exists_true(self):
        """Test exists method returns True for existing item."""
        # Mock fetch_one to return a row
        self.db_config.fetch_one.return_value = (1,)

        self.assertTrue(self.repo.exists("Grape"))

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT 1 FROM items WHERE name = ?', ("Grape",))

    def test_exists_false(self):
        """Test exists method returns False for nonexistent item."""
        # Mock fetch_one to return None
        self.db_config.fetch_one.return_value = None

        self.assertFalse(self.repo.exists("Nonexistent"))

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT 1 FROM items WHERE name = ?', ("Nonexistent",))

    def test_update_existing_item(self):
        """Test updating an existing item."""
        # Mock execute_query to return cursor with rowcount > 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 1
        self.db_config.execute_query.return_value = mock_cursor

        # Update item
        updated_item = ItemDto("Apple", 25, 1.75)
        result = self.repo.update(updated_item)
        self.assertTrue(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'UPDATE items SET quantity = ?, price = ? WHERE name = ?',
            (25, 1.75, "Apple")
        )

    def test_update_nonexistent_item(self):
        """Test updating a nonexistent item."""
        # Mock execute_query to return cursor with rowcount = 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 0
        self.db_config.execute_query.return_value = mock_cursor

        updated_item = ItemDto("Nonexistent", 25, 1.75)
        result = self.repo.update(updated_item)
        self.assertFalse(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'UPDATE items SET quantity = ?, price = ? WHERE name = ?',
            (25, 1.75, "Nonexistent")
        )

    def test_delete_existing_item(self):
        """Test deleting an existing item."""
        # Mock execute_query to return cursor with rowcount > 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 1
        self.db_config.execute_query.return_value = mock_cursor

        result = self.repo.delete("Apple")
        self.assertTrue(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'DELETE FROM items WHERE name = ?',
            ("Apple",)
        )

    def test_delete_nonexistent_item(self):
        """Test deleting a nonexistent item."""
        # Mock execute_query to return cursor with rowcount = 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 0
        self.db_config.execute_query.return_value = mock_cursor

        result = self.repo.delete("Nonexistent")
        self.assertFalse(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'DELETE FROM items WHERE name = ?',
            ("Nonexistent",)
        )

if __name__ == '__main__':
    unittest.main()