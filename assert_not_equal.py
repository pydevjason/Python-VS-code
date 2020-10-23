import unittest

# .assertNotEqual() is a complimentary method to .assertEqual() and takes two arguments which are checked against each other for inequality 

def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy

class TestInequality(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)
        self.assertNotEqual("Hello", "hello")
        self.assertNotEqual([1,2], [2,1])

    def test_copy_and_add_element(self):
        values = [1, 2, 3]
        result = copy_and_add_element(values, 4)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertNotEqual(
            values, 
            [1, 2, 3, 4], 
            "the copy_and_add_element() is a list mutation, make sure you're creating a copy"
        )


if __name__ == "__main__":
    unittest.main()