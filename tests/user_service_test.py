import unittest
from unittest.mock import Mock
from ..src.user.Service.UserService import UserService
from ..src.user.dto import UserDto

class TestUserService(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.mock_repo = Mock()
        self.service = UserService(self.mock_repo)
        self.mock_repo.reset_mock()

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        pass

    def test_create_user(self):
        """Test creating a new user."""
        user = UserDto("john_doe", "john@example.com", "password123")
        self.mock_repo.exists.return_value = False
        self.mock_repo.create.return_value = True

        result = self.service.create(user)
        self.assertTrue(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("john_doe")
        self.mock_repo.create.assert_called_once_with(user)

    def test_create_user_duplicate_username(self):
        """Test creating a user with duplicate username fails."""
        user = UserDto("john_doe", "john@example.com", "password123")
        self.mock_repo.exists.return_value = True

        result = self.service.create(user)
        self.assertFalse(result)

        # Verify exists was called, create was not
        self.mock_repo.exists.assert_called_once_with("john_doe")
        self.mock_repo.create.assert_not_called()

    def test_create_user_failure(self):
        """Test creating a user fails at repo level."""
        user = UserDto("john_doe", "john@example.com", "password123")
        self.mock_repo.exists.return_value = False
        self.mock_repo.create.return_value = False

        result = self.service.create(user)
        self.assertFalse(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("john_doe")
        self.mock_repo.create.assert_called_once_with(user)

    def test_get_all_users(self):
        """Test retrieving all users."""
        expected_users = [
            UserDto("john_doe", "john@example.com", "password123"),
            UserDto("jane_smith", "jane@example.com", "password456")
        ]
        self.mock_repo.get_all.return_value = expected_users

        users = self.service.get_all()
        self.assertEqual(users, expected_users)

        # Verify repo.get_all was called
        self.mock_repo.get_all.assert_called_once()

    def test_find_by_username_existing(self):
        """Test finding an existing user by username."""
        expected_user = UserDto("john_doe", "john@example.com", "password123")
        self.mock_repo.find_by_username.return_value = expected_user

        user = self.service.find_by_username("john_doe")
        self.assertEqual(user, expected_user)

        # Verify repo.find_by_username was called
        self.mock_repo.find_by_username.assert_called_once_with("john_doe")

    def test_find_by_username_nonexistent(self):
        """Test finding a nonexistent user by username."""
        self.mock_repo.find_by_username.return_value = None

        user = self.service.find_by_username("nonexistent")
        self.assertIsNone(user)

        # Verify repo.find_by_username was called
        self.mock_repo.find_by_username.assert_called_once_with("nonexistent")

    def test_find_by_email_existing(self):
        """Test finding an existing user by email."""
        expected_user = UserDto("john_doe", "john@example.com", "password123")
        self.mock_repo.find_by_email.return_value = expected_user

        user = self.service.find_by_email("john@example.com")
        self.assertEqual(user, expected_user)

        # Verify repo.find_by_email was called
        self.mock_repo.find_by_email.assert_called_once_with("john@example.com")

    def test_find_by_email_nonexistent(self):
        """Test finding a nonexistent user by email."""
        self.mock_repo.find_by_email.return_value = None

        user = self.service.find_by_email("nonexistent@example.com")
        self.assertIsNone(user)

        # Verify repo.find_by_email was called
        self.mock_repo.find_by_email.assert_called_once_with("nonexistent@example.com")

    def test_exists_true(self):
        """Test exists method returns True for existing user."""
        self.mock_repo.exists.return_value = True

        self.assertTrue(self.service.exists("john_doe"))

        # Verify repo.exists was called
        self.mock_repo.exists.assert_called_once_with("john_doe")

    def test_exists_false(self):
        """Test exists method returns False for nonexistent user."""
        self.mock_repo.exists.return_value = False

        self.assertFalse(self.service.exists("nonexistent"))

        # Verify repo.exists was called
        self.mock_repo.exists.assert_called_once_with("nonexistent")

    def test_update_user(self):
        """Test updating an existing user."""
        user = UserDto("john_doe", "john_new@example.com", "newpassword")
        self.mock_repo.exists.return_value = True
        self.mock_repo.update.return_value = True

        result = self.service.update(user)
        self.assertTrue(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("john_doe")
        self.mock_repo.update.assert_called_once_with(user)

    def test_update_user_nonexistent(self):
        """Test updating a nonexistent user fails."""
        user = UserDto("nonexistent", "new@example.com", "newpassword")
        self.mock_repo.exists.return_value = False

        result = self.service.update(user)
        self.assertFalse(result)

        # Verify exists was called, update was not
        self.mock_repo.exists.assert_called_once_with("nonexistent")
        self.mock_repo.update.assert_not_called()

    def test_update_user_failure(self):
        """Test updating a user fails at repo level."""
        user = UserDto("john_doe", "john_new@example.com", "newpassword")
        self.mock_repo.exists.return_value = True
        self.mock_repo.update.return_value = False

        result = self.service.update(user)
        self.assertFalse(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("john_doe")
        self.mock_repo.update.assert_called_once_with(user)

    def test_delete_existing_user(self):
        """Test deleting an existing user."""
        self.mock_repo.exists.return_value = True
        self.mock_repo.delete.return_value = True

        result = self.service.delete("john_doe")
        self.assertTrue(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("john_doe")
        self.mock_repo.delete.assert_called_once_with("john_doe")

    def test_delete_nonexistent_user(self):
        """Test deleting a nonexistent user fails."""
        self.mock_repo.exists.return_value = False

        result = self.service.delete("nonexistent")
        self.assertFalse(result)

        # Verify exists was called, delete was not
        self.mock_repo.exists.assert_called_once_with("nonexistent")
        self.mock_repo.delete.assert_not_called()

    def test_delete_user_failure(self):
        """Test deleting a user fails at repo level."""
        self.mock_repo.exists.return_value = True
        self.mock_repo.delete.return_value = False

        result = self.service.delete("john_doe")
        self.assertFalse(result)

        # Verify repo methods were called correctly
        self.mock_repo.exists.assert_called_once_with("john_doe")
        self.mock_repo.delete.assert_called_once_with("john_doe")

if __name__ == '__main__':
    unittest.main()