#!/usr/bin/python3
"""Unittest for the User class"""
from models import user
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def test_documentation(self):
        """Test for documentation in the module and class"""
        self.assertTrue(len(user.__doc__) > 1)
        self.assertTrue(len(User.__doc__) > 1)

    def test_attributes(self):
        """Test the attributes"""
        instance = User()
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.last_name, str)

if __name__ == "__main__":
    """Executes the test cases"""
    unittest.main()
