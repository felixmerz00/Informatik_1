from average_file import average
from unittest import TestCase

class Test_Average(TestCase):
    def test_empty_list(self):
        actual = average([])
        self.assertEqual(actual, None)
    def test_list_valid(self):
        actual = average([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(actual, 5)
    def test_list_invalid(self):
        # self.assertRaises(TypeError, average([1, 2, 3, 4, 5, 'a', 7, 8, 9,]))
        with self.assertRaises(TypeError, msg = "Invalid input."):
            average([1, 2, 3, 4, 5, 'a', 7, 8, 9,])

t = Test_Average()
t.test_empty_list()
t.test_list_valid()
t.test_list_invalid()