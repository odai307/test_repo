#!/usr/bin/python3

"""
Model for testing the city model
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Class for testing features/funtionality of the city class/object
    """
    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(City.__doc__), 0)
