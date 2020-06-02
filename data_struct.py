import unittest

class DataTests(unittest.TestCase):

    def setUp(self):
        self.data = {}

    def tearDown(self):
        del self.data

    def test_empty_struct(self):
        self.assertEqual(self.data, {})

if __name__ == "__main__":
    unittest.main()
