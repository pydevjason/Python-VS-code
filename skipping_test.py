import unittest

class TestSkippingStuff(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(10 - 5, 5)

    @unittest.skip("To be implemented later")
    def test_multiplication(self):
        pass

if __name__ == "__main__":
    unittest.main()


# this script shows how to implement a skipping scenario while testing code if I needed to skip an instance method and come back to it at a later time.  using the @property notation with the .skip() method that accepts a string argument where notes can be placed.  