#!/usr/bin/python3
"""
Unittests for the `Base` class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_assignment(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_manual_id_assignment(self):
        """Test assigning a specific ID."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None argument."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Test to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid_list(self):
        """Test to_json_string with a valid list of dictionaries."""
        list_dicts = [{'id': 12}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, '[{"id": 12}]')
        self.assertIsInstance(json_str, str)

    def test_from_json_string_none(self):
        """Test from_json_string with None argument."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid_string(self):
        """Test from_json_string with a valid JSON string."""
        json_str = '[{"id": 89}]'
        list_dicts = Base.from_json_string(json_str)
        self.assertEqual(list_dicts, [{'id': 89}])
        self.assertIsInstance(list_dicts, list)

if __name__ == '__main__':
    unittest.main()