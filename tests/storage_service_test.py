import pytest
import unittest
from unittest.mock import Mock
from ..src.storage.Service.StorageService import StorageService
from ..src.storage.dto import ItemDto

class TestStorageService(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.mock_repo = Mock()
        self.service = StorageService(self.mock_repo)
        self.mock_repo.reset_mock()

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        pass
    
    @pytest.mark.add_item
    def test_create_item(self):
        """Test creating a new item."""
        item = ItemDto("Apple", 10, 1.50)
        self.mock_repo.exists.return_value = False
        self.mock_repo.create.return_value = True

        result = self.service.create(item)
        self.assertTrue(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("Apple")
        self.mock_repo.create.assert_called_once_with(item)

    @pytest.mark.add_item
    def test_create_item_duplicate(self):
        """Test creating an item with duplicate name fails."""
        item = ItemDto("Apple", 10, 1.50)
        self.mock_repo.exists.return_value = True

        result = self.service.create(item)
        self.assertFalse(result)

        # Verify exists was called, create was not
        self.mock_repo.exists.assert_called_once_with("Apple")
        self.mock_repo.create.assert_not_called()

    @pytest.mark.add_item
    def test_create_item_failure(self):
        """Test creating an item fails at repo level."""
        item = ItemDto("Apple", 10, 1.50)
        self.mock_repo.exists.return_value = False
        self.mock_repo.create.return_value = False

        result = self.service.create(item)
        self.assertFalse(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("Apple")
        self.mock_repo.create.assert_called_once_with(item)

    @pytest.mark.add_item
    def test_create_item_invalid_name(self):
        """Test creating an item with invalid name fails."""
        item = ItemDto("", 10, 1.50)

        result = self.service.create(item)
        self.assertFalse(result)

        # Verify repo methods were not called
        self.mock_repo.exists.assert_not_called()
        self.mock_repo.create.assert_not_called()

    @pytest.mark.add_item
    def test_create_item_negative_quantity(self):
        """Test creating an item with negative quantity fails."""
        item = ItemDto("Apple", -1, 1.50)

        result = self.service.create(item)
        self.assertFalse(result)

        # Verify repo methods were not called
        self.mock_repo.exists.assert_not_called()
        self.mock_repo.create.assert_not_called()

    @pytest.mark.add_item
    def test_create_item_negative_price(self):
        """Test creating an item with negative price fails."""
        item = ItemDto("Apple", 10, -1.50)

        result = self.service.create(item)
        self.assertFalse(result)

        # Verify repo methods were not called
        self.mock_repo.exists.assert_not_called()
        self.mock_repo.create.assert_not_called()

    @pytest.mark.get_all_items
    def test_get_all_items(self):
        """Test retrieving all items."""
        expected_items = [
            ItemDto("Apple", 10, 1.50),
            ItemDto("Banana", 20, 0.75)
        ]
        self.mock_repo.get_all.return_value = expected_items

        items = self.service.get_all()
        self.assertEqual(items, expected_items)

        # Verify repo.get_all was called
        self.mock_repo.get_all.assert_called_once()

    @pytest.mark.find_item_by_name
    def test_find_by_name_existing(self):
        """Test finding an existing item by name."""
        expected_item = ItemDto("Orange", 15, 2.00)
        self.mock_repo.find_by_name.return_value = expected_item

        item = self.service.find_by_name("Orange")
        self.assertEqual(item, expected_item)

        # Verify repo.find_by_name was called
        self.mock_repo.find_by_name.assert_called_once_with("Orange")

    @pytest.mark.find_item_by_name
    def test_find_by_name_nonexistent(self):
        """Test finding a nonexistent item by name."""
        self.mock_repo.find_by_name.return_value = None

        item = self.service.find_by_name("Nonexistent")
        self.assertIsNone(item)

        # Verify repo.find_by_name was called
        self.mock_repo.find_by_name.assert_called_once_with("Nonexistent")

    @pytest.mark.item_exists
    def test_exists_true(self):
        """Test exists method returns True for existing item."""
        self.mock_repo.exists.return_value = True

        self.assertTrue(self.service.exists("Grape"))

        # Verify repo.exists was called
        self.mock_repo.exists.assert_called_once_with("Grape")

    @pytest.mark.item_exists
    def test_exists_false(self):
        """Test exists method returns False for nonexistent item."""
        self.mock_repo.exists.return_value = False

        self.assertFalse(self.service.exists("Nonexistent"))

        # Verify repo.exists was called
        self.mock_repo.exists.assert_called_once_with("Nonexistent")

    @pytest.mark.update_item
    def test_update_item(self):
        """Test updating an existing item."""
        item = ItemDto("Apple", 25, 1.75)
        self.mock_repo.exists.return_value = True
        self.mock_repo.update.return_value = True

        result = self.service.update(item)
        self.assertTrue(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("Apple")
        self.mock_repo.update.assert_called_once_with(item)

    @pytest.mark.update_item
    def test_update_item_nonexistent(self):
        """Test updating a nonexistent item fails."""
        item = ItemDto("Nonexistent", 25, 1.75)
        self.mock_repo.exists.return_value = False

        result = self.service.update(item)
        self.assertFalse(result)

        # Verify exists was called, update was not
        self.mock_repo.exists.assert_called_once_with("Nonexistent")
        self.mock_repo.update.assert_not_called()

    @pytest.mark.update_item
    def test_update_item_failure(self):
        """Test updating an item fails at repo level."""
        item = ItemDto("Apple", 25, 1.75)
        self.mock_repo.exists.return_value = True
        self.mock_repo.update.return_value = False

        result = self.service.update(item)
        self.assertFalse(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("Apple")
        self.mock_repo.update.assert_called_once_with(item)

    @pytest.mark.update_item
    def test_update_item_invalid_name(self):
        """Test updating an item with invalid name fails."""
        item = ItemDto("", 25, 1.75)

        result = self.service.update(item)
        self.assertFalse(result)

        # Verify repo methods were not called
        self.mock_repo.exists.assert_not_called()
        self.mock_repo.update.assert_not_called()

    @pytest.mark.update_item
    def test_update_item_negative_quantity(self):
        """Test updating an item with negative quantity fails."""
        item = ItemDto("Apple", -1, 1.75)

        result = self.service.update(item)
        self.assertFalse(result)

        # Verify repo methods were not called
        self.mock_repo.exists.assert_not_called()
        self.mock_repo.update.assert_not_called()

    @pytest.mark.update_item
    def test_update_item_negative_price(self):
        """Test updating an item with negative price fails."""
        item = ItemDto("Apple", 25, -1.75)

        result = self.service.update(item)
        self.assertFalse(result)

        # Verify repo methods were not called
        self.mock_repo.exists.assert_not_called()
        self.mock_repo.update.assert_not_called()

    @pytest.mark.delete_item
    def test_delete_existing_item(self):
        """Test deleting an existing item."""
        self.mock_repo.exists.return_value = True
        self.mock_repo.delete.return_value = True

        result = self.service.delete("Apple")
        self.assertTrue(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("Apple")
        self.mock_repo.delete.assert_called_once_with("Apple")

    @pytest.mark.delete_item
    def test_delete_nonexistent_item(self):
        """Test deleting a nonexistent item fails."""
        self.mock_repo.exists.return_value = False

        result = self.service.delete("Nonexistent")
        self.assertFalse(result)

        # Verify exists was called, delete was not
        self.mock_repo.exists.assert_called_once_with("Nonexistent")
        self.mock_repo.delete.assert_not_called()

    @pytest.mark.delete_item
    def test_delete_item_failure(self):
        """Test deleting an item fails at repo level."""
        self.mock_repo.exists.return_value = True
        self.mock_repo.delete.return_value = False

        result = self.service.delete("Apple")
        self.assertFalse(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("Apple")
        self.mock_repo.delete.assert_called_once_with("Apple")

if __name__ == '__main__':
    unittest.main()