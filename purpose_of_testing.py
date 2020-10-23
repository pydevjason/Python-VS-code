import unittest

# def multiply(a, b):
#     return a + b

# class MultiplyTestCase(unittest.TestCase):
#     def test_multiply(self):
#         self.assertEqual(multiply(3, 4), 12)

# if __name__ == "__main__":
#     unittest.main()

class TestStringMethods(unittest.TestCase):

    def test_split(self):

      self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])



    def test_count(self):

      self.assertEqual("beautiful".count("u"), 2)

    def test_swapcase(self):

      self.assertEqual("FiSh".swapcase(), "fIsH")
      self.assertEqual("yOkE".swapcase(), "YoKe")

    def test_index(self):

      self.assertEqual("mode".index("m"), 0)
      self.assertEqual("wilt".index("t"), 3)


if __name__ == "__main__":

  unittest.main()
