import os
import unittest

def file_exists(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)

class TestFileExists(unittest.TestCase):
    def test_existing_file(self):
        directory = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day14'
        filename = 'calculator.py'
        self.assertTrue(file_exists(directory, filename), "The file exists in the specified directory")

    def test_nonexistent_file(self):
        directory = r'C:\Users\harsh\Desktop\harsha_wipro\python\Day14'
        filename = 'calsi.py'
        self.assertFalse(file_exists(directory, filename), "The file not exists in the specified directory")

if __name__ == '__main__':
    unittest.main()