#!/usr/bin/python3
"""
Model for testing amenity class 
"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    class for testing Amenity objects
    """
    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(Amenity.__doc__), 0)
