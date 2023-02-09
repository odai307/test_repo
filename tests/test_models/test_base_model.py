#!/usr/bin/python3

"""Model for testing the BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """For testing most/all possible scenarios"""

    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(BaseModel.__doc__), 0)
