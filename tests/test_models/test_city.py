#!/usr/bin/python3
"""Unittest for City class"""
from models.city import City
from models import city
import unittest


class TestCity(unittest.TestCase):
    """Test the class City"""

    def test_documentation(self):
        """Test for documentation in the module and the class"""
        self.assertTrue(len(city.__doc__) > 1)
        self.assertTrue(len(City.__doc__) > 1)

    def test_attributes(self):
        """Test the attributes of an instance"""
        instance = City()
        self.assertIsInstance(instance.id, str)

if __name__ == "__main__":
    """Executes the test"""
    unittest.main()
