import unittest


def add_numbers(a, b):
    return a + b



class AddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        print(self.assertEqual(add_numbers(2, 2), 4))


if __name__ == "__main__":
    unittest.main()