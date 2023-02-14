#!/usr/bin/pyhon3

"""
Model for testing the review model
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Class for testing review class
    """
    def test_class_documentation(self):
        """testing if class is documented"""
        self.assertGreater(len(Review.__doc__), 0)
