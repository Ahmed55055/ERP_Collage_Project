import unittest
from unittest.mock import Mock
from ..src.user.Repository.UserRepository import UserRepository
from ..src.user.dto import UserDto

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.db_config = Mock()
        self.repo = UserRepository(self.db_config)
        self.db_config.reset_mock()

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        pass

    def test_create_user(self):
        """Test creating a new user."""
        user = UserDto("john_doe", "john@example.com", "password123")
        result = self.repo.create(user)
        self.assertTrue(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            ("john_doe", "john@example.com", "password123")
        )

    def test_create_duplicate_username(self):
        """Test creating a user with duplicate username fails."""
        user1 = UserDto("john_doe", "john@example.com", "password123")
        user2 = UserDto("john_doe", "john2@example.com", "password456")

        # First create succeeds
        result1 = self.repo.create(user1)
        self.assertTrue(result1)

        # Mock second create to raise exception (duplicate)
        self.db_config.execute_query.side_effect = Exception("Duplicate username")

        result2 = self.repo.create(user2)
        self.assertFalse(result2)

        # Verify calls
        self.assertEqual(self.db_config.execute_query.call_count, 2)

    def test_create_duplicate_email(self):
        """Test creating a user with duplicate email fails."""
        user1 = UserDto("john_doe", "john@example.com", "password123")
        user2 = UserDto("jane_doe", "john@example.com", "password456")

        # First create succeeds
        result1 = self.repo.create(user1)
        self.assertTrue(result1)

        # Mock second create to raise exception (duplicate)
        self.db_config.execute_query.side_effect = Exception("Duplicate email")

        result2 = self.repo.create(user2)
        self.assertFalse(result2)

        # Verify calls
        self.assertEqual(self.db_config.execute_query.call_count, 2)

    def test_get_all_users(self):
        """Test retrieving all users."""
        # Mock fetch_all to return test data
        self.db_config.fetch_all.return_value = [
            ("john_doe", "john@example.com", "password123"),
            ("jane_smith", "jane@example.com", "password456")
        ]

        users = self.repo.get_all()
        self.assertEqual(len(users), 2)

        # Check users are returned as DTOs
        usernames = [user.username for user in users]
        self.assertIn("john_doe", usernames)
        self.assertIn("jane_smith", usernames)

        # Verify fetch_all was called
        self.db_config.fetch_all.assert_called_once_with('SELECT username, email, password FROM users')

    def test_find_by_username_existing(self):
        """Test finding an existing user by username."""
        # Mock fetch_one to return data
        self.db_config.fetch_one.return_value = ("john_doe", "john@example.com", "password123")

        user = self.repo.find_by_username("john_doe")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password123")

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT username, email, password FROM users WHERE username = ?', ("john_doe",))

    def test_find_by_username_nonexistent(self):
        """Test finding a nonexistent user by username."""
        # Mock fetch_one to return None
        self.db_config.fetch_one.return_value = None

        user = self.repo.find_by_username("nonexistent")
        self.assertIsNone(user)

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT username, email, password FROM users WHERE username = ?', ("nonexistent",))

    def test_find_by_email_existing(self):
        """Test finding an existing user by email."""
        # Mock fetch_one to return data
        self.db_config.fetch_one.return_value = ("john_doe", "john@example.com", "password123")

        user = self.repo.find_by_email("john@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john@example.com")

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT username, email, password FROM users WHERE email = ?', ("john@example.com",))

    def test_find_by_email_nonexistent(self):
        """Test finding a nonexistent user by email."""
        # Mock fetch_one to return None
        self.db_config.fetch_one.return_value = None

        user = self.repo.find_by_email("nonexistent@example.com")
        self.assertIsNone(user)

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT username, email, password FROM users WHERE email = ?', ("nonexistent@example.com",))

    def test_exists_true(self):
        """Test exists method returns True for existing user."""
        # Mock fetch_one to return a row
        self.db_config.fetch_one.return_value = (1,)

        self.assertTrue(self.repo.exists("john_doe"))

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT 1 FROM users WHERE username = ?', ("john_doe",))

    def test_exists_false(self):
        """Test exists method returns False for nonexistent user."""
        # Mock fetch_one to return None
        self.db_config.fetch_one.return_value = None

        self.assertFalse(self.repo.exists("nonexistent"))

        # Verify fetch_one was called
        self.db_config.fetch_one.assert_called_once_with('SELECT 1 FROM users WHERE username = ?', ("nonexistent",))

    def test_update_existing_user(self):
        """Test updating an existing user."""
        # Mock execute_query to return cursor with rowcount > 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 1
        self.db_config.execute_query.return_value = mock_cursor

        # Update user
        updated_user = UserDto("john_doe", "john_new@example.com", "newpassword")
        result = self.repo.update(updated_user)
        self.assertTrue(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'UPDATE users SET email = ?, password = ? WHERE username = ?',
            ("john_new@example.com", "newpassword", "john_doe")
        )

    def test_update_nonexistent_user(self):
        """Test updating a nonexistent user."""
        # Mock execute_query to return cursor with rowcount = 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 0
        self.db_config.execute_query.return_value = mock_cursor

        updated_user = UserDto("nonexistent", "new@example.com", "newpassword")
        result = self.repo.update(updated_user)
        self.assertFalse(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'UPDATE users SET email = ?, password = ? WHERE username = ?',
            ("new@example.com", "newpassword", "nonexistent")
        )

    def test_delete_existing_user(self):
        """Test deleting an existing user."""
        # Mock execute_query to return cursor with rowcount > 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 1
        self.db_config.execute_query.return_value = mock_cursor

        result = self.repo.delete("john_doe")
        self.assertTrue(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'DELETE FROM users WHERE username = ?',
            ("john_doe",)
        )

    def test_delete_nonexistent_user(self):
        """Test deleting a nonexistent user."""
        # Mock execute_query to return cursor with rowcount = 0
        mock_cursor = Mock()
        mock_cursor.rowcount = 0
        self.db_config.execute_query.return_value = mock_cursor

        result = self.repo.delete("nonexistent")
        self.assertFalse(result)

        # Verify execute_query was called correctly
        self.db_config.execute_query.assert_called_once_with(
            'DELETE FROM users WHERE username = ?',
            ("nonexistent",)
        )

if __name__ == '__main__':
    unittest.main()