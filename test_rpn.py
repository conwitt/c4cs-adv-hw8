"""
Tests for rpn.py
"""

import unittest
import rpn

class TestBasics(unittest.TestCase):
    """
    Basic tests for rpn.y
    """
    def test_add(self):
        """
        Test for addition
        """
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
