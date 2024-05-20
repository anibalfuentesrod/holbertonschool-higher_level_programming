#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        """Test max integer at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_middle(self):
        """Test max integer in the middle of the list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test max integer at the beginning of the list"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_all_negative(self):
        """Test list with all negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test list with mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_same_elements(self):
        """Test list with all elements being the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_float_elements(self):
        """Test list with float elements"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_string_elements(self):
        """Test list with string elements"""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_none(self):
        """Test list with None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_integers(self):
        """Test list with non-integer types"""
        with self.assertRaises(TypeError):
            max_integer(["a", 1, None])


if __name__ == '__main__':
    unittest.main()
