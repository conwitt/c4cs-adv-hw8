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

    def test_subtract(self):
        """
        Test for subtraction
        """
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)

    def test_multiply(self):
        """
        Test for multiplication
        """
        result = rpn.calculate('5 6 *')
        self.assertEqual(30, result)

    def test_divide(self):
        """
        Test for division
        """
        result = rpn.calculate('30 6 /')
        self.assertEqual(5, result)
