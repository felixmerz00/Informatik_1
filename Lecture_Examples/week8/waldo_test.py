from where_is_waldo import find_waldo
from unittest import TestCase

class Waldo_Test(TestCase):
    def test_in_list(self):
        names = ["Wuldo", "Waldo", "Wildo", "Woldo"]
        actual = find_waldo(names)
        self.assertEqual(actual, 1)
    def test_empty_list(self):
        names = []
        actual = find_waldo(names)
        self.assertEqual(actual, None)
    def test_not_in_list(self):
        names = ["Wuldo", "Weldo", "Wildo", "Woldo"]
        actual = find_waldo(names)
        self.assertEqual(actual, None)

t = Waldo_Test()
t.test_in_list()
t.test_empty_list()
t.test_not_in_list()