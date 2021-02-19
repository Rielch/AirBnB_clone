#!/usr/bin/python3
"""Unittest for City class"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Test the class City"""

    def test_attributes(self):
        """Test the attributes of an instance"""
        instance = City()
        self.assertIsInstance(instance.id, str)
        self.assertEqual(instance.created_at, instance.updated_at)

if __name__ == "__main__":
    """Executes the test"""
    unittest.main()
