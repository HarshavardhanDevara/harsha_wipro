import unittest
def is_palindrome(string):
    return string == string[::-1]
class TestPalindrome(unittest.TestCase):
    def test_palindrome_string(self):
        x = "madam"
        print("Test  palindrome:", x)
        self.assertTrue(is_palindrome(x), "The string is a palindrome")
    def test_non_palindrome_string(self):
        x= "hello"
        print("Test non palindrome:", x)
        self.assertFalse(is_palindrome(x), "The string is not a palindrome")