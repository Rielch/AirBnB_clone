#!/usr/bin/python3
"""Unittest for Amenity class"""
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Class to thest the class Amenity"""

    def test_attributes(self):
        """Test the attributes"""
        instance = Amenity()
        self.assertIsInstance(instance.id, str)


if __name__ == "__main__":
    """Executes the test"""
    unittest.main()
