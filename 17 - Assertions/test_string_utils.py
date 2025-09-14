from string_utils import reverse_string, capitalize_string, is_capitalized
import unittest

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"),"olleh")
    
    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
    
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Hello"), "The string should be capitalized")
        
    

if __name__ == '__main__':
    unittest.main()