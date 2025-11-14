import unittest
import os
from user.UserRepository import UserRepository
from user.dto import UserDto
from database.config import DatabaseConfig

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_db = ':memory:'
        self.db_config = DatabaseConfig(self.test_db)
        self.repo = UserRepository(self.db_config)

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

    def test_create_user(self):
        """Test creating a new user."""
        user = UserDto("john_doe", "john@example.com", "password123")
        result = self.repo.create(user)
        self.assertTrue(result)

        # Verify user was created
        found_user = self.repo.find_by_username("john_doe")
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.username, "john_doe")
        self.assertEqual(found_user.email, "john@example.com")
        self.assertEqual(found_user.password, "password123")

    def test_create_duplicate_username(self):
        """Test creating a user with duplicate username fails."""
        user1 = UserDto("john_doe", "john@example.com", "password123")
        user2 = UserDto("john_doe", "john2@example.com", "password456")

        result1 = self.repo.create(user1)
        result2 = self.repo.create(user2)

        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_create_duplicate_email(self):
        """Test creating a user with duplicate email fails."""
        user1 = UserDto("john_doe", "john@example.com", "password123")
        user2 = UserDto("jane_doe", "john@example.com", "password456")

        result1 = self.repo.create(user1)
        result2 = self.repo.create(user2)

        self.assertTrue(result1)
        self.assertFalse(result2)

    def test_get_all_users(self):
        """Test retrieving all users."""
        # Create test users
        self.repo.create(UserDto("john_doe", "john@example.com", "password123"))
        self.repo.create(UserDto("jane_smith", "jane@example.com", "password456"))

        users = self.repo.get_all()
        self.assertEqual(len(users), 2)

        # Check users are returned as DTOs
        usernames = [user.username for user in users]
        self.assertIn("john_doe", usernames)
        self.assertIn("jane_smith", usernames)

    def test_find_by_username_existing(self):
        """Test finding an existing user by username."""
        self.repo.create(UserDto("john_doe", "john@example.com", "password123"))

        user = self.repo.find_by_username("john_doe")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john@example.com")
        self.assertEqual(user.password, "password123")

    def test_find_by_username_nonexistent(self):
        """Test finding a nonexistent user by username."""
        user = self.repo.find_by_username("nonexistent")
        self.assertIsNone(user)

    def test_find_by_email_existing(self):
        """Test finding an existing user by email."""
        self.repo.create(UserDto("john_doe", "john@example.com", "password123"))

        user = self.repo.find_by_email("john@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "john_doe")
        self.assertEqual(user.email, "john@example.com")

    def test_find_by_email_nonexistent(self):
        """Test finding a nonexistent user by email."""
        user = self.repo.find_by_email("nonexistent@example.com")
        self.assertIsNone(user)

    def test_exists_true(self):
        """Test exists method returns True for existing user."""
        self.repo.create(UserDto("john_doe", "john@example.com", "password123"))
        self.assertTrue(self.repo.exists("john_doe"))

    def test_exists_false(self):
        """Test exists method returns False for nonexistent user."""
        self.assertFalse(self.repo.exists("nonexistent"))

    def test_update_existing_user(self):
        """Test updating an existing user."""
        # Create initial user
        self.repo.create(UserDto("john_doe", "john@example.com", "password123"))

        # Update user
        updated_user = UserDto("john_doe", "john_new@example.com", "newpassword")
        result = self.repo.update(updated_user)
        self.assertTrue(result)

        # Verify update
        found_user = self.repo.find_by_username("john_doe")
        self.assertEqual(found_user.email, "john_new@example.com")
        self.assertEqual(found_user.password, "newpassword")

    def test_update_nonexistent_user(self):
        """Test updating a nonexistent user."""
        updated_user = UserDto("nonexistent", "new@example.com", "newpassword")
        result = self.repo.update(updated_user)
        self.assertFalse(result)

    def test_delete_existing_user(self):
        """Test deleting an existing user."""
        self.repo.create(UserDto("john_doe", "john@example.com", "password123"))

        result = self.repo.delete("john_doe")
        self.assertTrue(result)

        # Verify deletion
        self.assertFalse(self.repo.exists("john_doe"))

    def test_delete_nonexistent_user(self):
        """Test deleting a nonexistent user."""
        result = self.repo.delete("nonexistent")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()