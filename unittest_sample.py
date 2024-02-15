import unittest


def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)
print(result)


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        print(self.assertEqual(add_numbers(2, 2), 4))

    def test_add_neg_numbers(self):
        print(self.assertEqual(add_numbers(-2, -2), -4))

x=TestAddNumbers()
x.test_add_numbers()
x.test_add_neg_numbers()