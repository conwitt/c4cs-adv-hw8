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

    def test_modulo(self):
        """
        Test for modulo divisiion
        """
        result0 = self.calc.calculate('6 4 %')
        result1 = self.calc.calculate('6 3 %')
        self.assertEqual(2, result0)
        self.assertEqual(0, result1)

    def test_exponent(self):
        """
        Test for exponentiation
        """
        result = self.calc.calculate('3 2 ^')
        self.assertEqual(9, result)
