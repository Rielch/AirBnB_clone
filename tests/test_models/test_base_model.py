#!/usr/bin/python3
"""Unittest to test the BaseModel class"""
from models.base_model import BaseModel
from models import base_model
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class with tests for BaseModel class"""


    def test_documentation(self):
        """Test for documentation in the module, class and methods"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(base_model.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_attributes(self):
        """Test the attributes of the BaseModel class"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        #Test id
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertIsInstance(instance1.id, str)
        #Test created_at
        self.assertEqual(instance1.created_at, instance1.updated_at)
        self.assertIsInstance(instance1.created_at, datetime)
        #Test updated_at
        self.assertEqual(update1, instance1.created_at)

    def test___init__(self):
        """Test the __init__ method"""
        inst_dict = {'created_at': datetime.datetime(2021, 2, 19, 2,
                                                     36, 21, 947456),
                     'updated_at': datetime.datetime(2021, 2, 19, 2,
                                                     36, 21, 947491),
                     'id': '04121eba-7ce3-444e-90de-4963d8e76096'}
        instance1 = BaseModel(**inst_dict)
        self.assertEqual(instance1.id, '04121eba-7ce3-444e-90de-4963d8e76096')

    def test_save(self):
        """Test the save method"""
        instance1 = BaseModel()
        update1 = instance1.updated_at
        isntance1.save()
        update2 = instance2.updated_at
        self.assertNotEqual(update1, update2)

    def test_to_dict(self):
        """Test the to_dict method"""
        instance1 = BaseModel()
        inst_dict = instance1.to_dict()
        self.assertIsInstance(inst_dict, dict)

    def test___str__(self):
        """Test the __str__ method"""
        instance1 = BaseModel()
        inst_str = instance1.__str__()
        self.assertIsInstance(inst_str, str)


if __name__ == "__main__":
    """Executes test cases"""
    unittest.main()
