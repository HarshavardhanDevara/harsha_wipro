import unittest
import sqlite3
class TestDatabaseConnection(unittest.TestCase):
    def test_database_connection(self):
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        self.assertEqual(result, (1,))
if __name__== '__main__':
    unittest.main()