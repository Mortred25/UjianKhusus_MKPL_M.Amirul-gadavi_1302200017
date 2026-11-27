import unittest
from main import tambah

class TestMain(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
        self.assertEqual(tambah(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
