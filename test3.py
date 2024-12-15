import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        # A simple addition test
        self.assertEqual(2 + 3, 5)

    def test_string_manipulation(self):
        # A test to check string manipulation
        string = "hello"
        self.assertEqual(string.upper(), "HELLO")

if __name__ == '__main__':
    unittest.main()
