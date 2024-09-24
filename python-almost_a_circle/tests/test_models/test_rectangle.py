#!/usr/bin/python3
"""
Unittests for the `Rectangle` class
"""
import unittest
from models.rectangle import Rectangle
import io
import contextlib
import os


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_instantiation(self):
        """Test creating Rectangle instances with various arguments."""

        # Valid instantiations
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        r2 = Rectangle(10, 2, 3)
        self.assertIsInstance(r2, Rectangle)
        r3 = Rectangle(10, 2, 3, 4)
        self.assertIsInstance(r3, Rectangle)
        r4 = Rectangle(10, 2, 3, 4, 5)
        self.assertIsInstance(r4, Rectangle)

        # Invalid instantiations (should raise TypeErrors)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        # Invalid instantiations (should raise ValueErrors)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test the area method."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Test the __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        """Test the display method without x and y."""
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display_no_y(self):
        """Test the display method without y."""
        r = Rectangle(2, 3, 1)
        expected_output = " ##\n ##\n ##\n"
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_display(self):
        """Test the display method with x and y."""
        r = Rectangle(2, 3, 1, 2)
        expected_output = "\n\n ##\n ##\n ##\n"
        with io.StringIO() as buf, contextlib.redirect_stdout(buf):
            r.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_update_args(self):
        """Test the update method with *args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 1)

    def test_create(self):
        """Test the create class method."""
        r1_dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
         
		 
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        # Test with an empty list as argument
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")


        os.remove("Rectangle.json")

    def test_load_from_file(self):
        """Test the load_from_file class method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output),2)

        # Cleanup
        os.remove("Rectangle.json")

if __name__ == '__main__':
    unittest.main()

