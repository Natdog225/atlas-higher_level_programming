import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    
    def test_create_square(self):
        """Test creating a square instance."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_invalid_size_type(self):
        """Test invalid size type raises TypeError."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_invalid_size_value(self):
        """Test invalid size value raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_str_method(self):
        """Test the __str__ method of Square."""
        s = Square(5, 2, 1, 10)
        self.assertEqual(str(s), "[Square] (10) 2/1 - 5")

    def test_to_dictionary(self):
        """Test the to_dictionary method of Square."""
        s = Square(10, 2, 1, 9)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 9, 'size': 10, 'x': 2, 'y': 1})

    def test_update_args(self):
        """Test the update method with *args."""
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

if __name__ == '__main__':
    unittest.main()
