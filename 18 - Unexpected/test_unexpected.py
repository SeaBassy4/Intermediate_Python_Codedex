from unexpected import get_sqrt, divide
import unittest

class TestUnexpected(unittest.TestCase): 
    def test_get_sqrt(self):
        self.assertEqual(get_sqrt(16), 4)
        self.assertEqual(get_sqrt(25), 5)
        with self.assertRaises(ValueError):
            get_sqrt(-4)
    
    def test_divide(self):
        self.assertEqual(divide(10,2), 5)
        self.assertEqual(divide(9,3), 3)
        with self.assertRaises(ZeroDivisionError):
            divide(5,0)


if __name__ == '__main__':
    unittest.main()