"""
Tests for rpn.py
"""

import unittest
from rpn import Calculator

class TestBasics(unittest.TestCase):
    """
    Basic tests for rpn.y
    """
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        """
        Test for addition
        """
        result = self.calc.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_subtract(self):
        """
        Test for subtraction
        """
        result = self.calc.calculate('5 3 -')
        self.assertEqual(2, result)

    def test_multiply(self):
        """
        Test for multiplication
        """
        result = self.calc.calculate('5 6 *')
        self.assertEqual(30, result)

    def test_divide(self):
        """
        Test for division
        """
        result = self.calc.calculate('30 6 /')
        self.assertEqual(5, result)
