from unittest import TestCase
from week9 import SortedDict

class TestSortedDict(TestCase):
    def test_add_at_end(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(2, "bcd")
        actual = x.__str__()
        expected = "{1: abc, 2: bcd}"
        self.assertEqual(actual, expected)
    def test_add_middle(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(2, "bcd")
        x.add(4, "cde")
        x.add(5, "efg")
        x.add(3, "fgh")
        actual = x.__str__()
        expected = "{1: abc, 2: bcd, 3: fgh, 4: cde, 5: efg}"
        self.assertEqual(actual, expected)
    def test_add_beginning(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(2, "bcd")
        x.add(0, "a")
        actual = x.__str__()
        expected = "{0: a, 1: abc, 2: bcd}"
        self.assertEqual(actual, expected)
    def test_add_overwrite(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(2, "bcd")
        x.add(3, "fgh")
        x.add(1, "ab")
        actual = x.__str__()
        expected = "{1: ab, 2: bcd, 3: fgh}"
        self.assertEqual(actual, expected)

    def test_remove_existing_key(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(2, "bcd")
        x.add(3, "fgh")
        x.add(4, "cde")
        x.add(5, "efg")
        x.remove(5)
        actual = x.__str__()
        expected = "{1: abc, 2: bcd, 3: fgh, 4: cde}"
        self.assertEqual(actual, expected)
    def test_remove_non_existing_key(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(2, "bcd")
        x.add(3, "fgh")
        x.add(4, "cde")
        x.add(5, "efg")
        with self.assertRaises(IndexError):
            x.remove(6)
    
    def test_addition(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(3, "bcd")
        x.add(4, "fgh")
        y = SortedDict()
        y.add(2, "fgh")
        y.add(4, "cde")
        y.add(5, "efg")
        z = x + y
        actual = z.__str__()
        expected = "{1: abc, 2: fgh, 3: bcd, 4: cde, 5: efg}"
        self.assertEqual(actual, expected)

    def test_subtraction(self):
        x = SortedDict()
        x.add(1, "abc")
        x.add(2, "bcd")
        x.add(3, "fgh")
        x.add(4, "cde")
        x.add(5, "efg")
        y = SortedDict()
        y.add(2, "fgh")
        y.add(4, "cde")
        y.add(6, "efg")
        z = x - y
        actual = z.__str__()
        expected = "{1: abc, 3: fgh, 5: efg}"
        self.assertEqual(actual, expected)

        
t = TestSortedDict()
t.test_add_at_end()
t.test_add_middle()
t.test_add_beginning()
t.test_add_overwrite()
t.test_remove_existing_key()
t.test_remove_non_existing_key()
t.test_addition()
t.test_subtraction()