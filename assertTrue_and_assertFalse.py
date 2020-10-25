import unittest

class TruthinessAndFalsinessTests(unittest.TestCase):
    def test_truthiness(self):
        self.assertTrue(3 < 5)
        self.assertTrue(1)
        self.assertTrue("hello")
        self.assertTrue("a")
        self.assertTrue({"a": [1, 2, 3]})

    def test_falsiness(self):
        self.assertFalse(False)
        self.assertFalse("")
        self.assertFalse(0)
        self.assertFalse([])
        self.assertFalse({})

if __name__ == "__main__":
    unittest.main()