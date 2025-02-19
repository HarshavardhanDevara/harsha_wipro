import unittest

def is_prime(value):
    count = 0
    for i in range(2,value+1):
        if value % i == 0:
            count += 1
        if count == 2:
            return False
    return True

class TestPrimenumber(unittest.TestCase):
    def test_prime_number(self):
        value = 2
        self.assertTrue(is_prime(value))

    def test_non_prime(self):
        value = 4
        self.assertFalse(is_prime(value))

if __name__ == "__main__":
    unittest.main()