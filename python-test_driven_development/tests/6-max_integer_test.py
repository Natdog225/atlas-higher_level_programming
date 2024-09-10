#!/usr/bin/python3
"""
This module contains unit tests for the `max_integer` function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for the `max_integer` function.
    """

    def test_empty_list(self):
        """
        Tests an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """
        Tests a list with a single element.
        """
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """
        Tests a list of positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """
        Tests a list of negative integers.
        """
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_integers(self):
        """
        Tests a list with both positive and negative integers.
        """
        self.assertEqual(max_integer([-3, 5, 0, -2]), 5)

    def test_duplicates(self):
        """
        Tests a list with duplicate values.
        """
        self.assertEqual(max_integer([3, 7, 3, 9, 3]), 9)

    def test_floats(self):
        """
        Tests a list of floats.
        """
        self.assertEqual(max_integer([2.5, 3.1, 1.8, 4.2]), 4.2)

    def test_mixed_types(self):
        """
        Tests a list with mixed data types (should raise TypeError).
        """
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 3])