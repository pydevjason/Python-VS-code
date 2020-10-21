# testing code is writing code to ensure the validity of other code we have written.  A unittest is a test that tests a chunk of a larger application
import unittest
class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("d+e+f".split("+"), ["d", "e", "f"])

    def test_count(self):
        self.assertEqual("beautiful".count("u"), 2)


if __name__ == "__main__":
    unittest.main()