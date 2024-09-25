#!/usr/bin/python3
"""
Unittests for the `Square` class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_instantiation(self):
        """Test creating Square instances with various arguments."""

        # Valid instantiations
        s1 = Square(10)
        self.assertIsInstance(s1, Square)
        s2 = Square(10, 2)
        self.assertIsInstance(s2, Square)
        s3 = Square(10, 2, 3)
        self.assertIsInstance(s3, Square)
        s4 = Square("10")
        self.assertIsInstance(s4, Square)

        # Invalid instantiations (should raise TypeErrors)
        with self.assertRaises(TypeError):
            Square("1", 2)
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        # Invalid instantiations (should raise ValueErrors)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_area(self):
        """Test the area method."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_str(self):
        """Test the __str__ method."""
        s = Square(4, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 2/1 - 4")

    def test_display(self):
        """Test the display method."""
        s = Square(2, 1, 2)
        expected_output = "\n\n ##\n ##\n"
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            s.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s = Square(10, 2, 3)
        expected_dict = {'id': s.id, 'size': 10, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_update_args(self):
        """Test the update method with *args."""
        s = Square(10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 2)
        self.assertEqual(s.size, 2)
        s.update(89, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        s = Square(10)
        s.update(size=1)
        self.assertEqual(s.size, 1)
        s.update(size=2, x=3)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        s.update(size=2, x=3, y=4, id=89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_create(self):
        """Test the create class method."""
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_save_to_file(self):
        """Test the save_to_file class method."""
        s1 = Square(10)
        s2 = Square(2, 3)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            content = file.read()
            self.assertIsInstance(content, str)
            list_dicts = Square.from_json_string(content)
            self.assertEqual(len(list_dicts), 2)
            self.assertIsInstance(list_dicts, list)
            self.assertEqual(list_dicts[0], s1.to_dictionary())
            self.assertEqual(list_dicts[1], s2.to_dictionary())

        # Test with None as argument
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        # Test with an empty list as argument
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        # Cleanup
        os.remove("Square.json")

    def test_load_from_file(self):
        """Test the load_from_file class method."""
        s1 = Square(10)
        s2 = Square(2, 3)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()
        self.assertEqual(len(list_squares_output), 2)
        for sq in list_squares_output:
            self.assertIsInstance(sq, Square)

        # Cleanup
        os.remove("Square.json")

if __name__ == '__main__':
    unittest.main()