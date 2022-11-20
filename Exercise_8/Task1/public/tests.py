#!/usr/bin/env python3

from unittest import TestCase
from script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    # Test empty profanity list
    def test_empty_list1(self):
        f = ProfanityFilter([], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi mastard jklmno"
        self.assertEqual(expected, actual)

    # Test empty msg
    def test_empty_msg1(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = ""
        actual = f.filter(msg)
        expected = ""
        self.assertEqual(expected, actual)

    # Test case sensitivity
    def test_case_sensitivity1(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi Mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    # Offensive word occurs as subword
    def test_subword(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi helmastardlo jklmno"
        actual = f.filter(msg)
        expected = "abc defghi hel?#$?#$?lo jklmno"
        self.assertEqual(expected, actual) 

    # Profanity is concatenation of other profanities
    def test_profanity_contains_each_other1(self):
        f = ProfanityFilter(["duck", "shotduck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi shotduck jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$?# jklmno"
        self.assertEqual(expected, actual)

    # Profanity is a subword and case sensitive
    def test_complex1(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi helMastardlo jklmno"
        actual = f.filter(msg)
        expected = "abc defghi hel?#$?#$?lo jklmno"
        self.assertEqual(expected, actual) 

    # One profanity in the middle of one word twice with different casing
    def test_complex2(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklShoTshOtmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jkl?#$??#$?mno"
        self.assertEqual(expected, actual)

    # Test upper case profanity list
    def test_upper_case_profanity(self):
        f = ProfanityFilter(["Duck", "Shot", "Batch", "Mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)


t = PublicTestSuite()
t.test_example()
t.test_empty_list1()
t.test_empty_msg1()
t.test_case_sensitivity1()
t.test_subword()
t.test_profanity_contains_each_other1()
t.test_complex1()
t.test_complex2()
t.test_upper_case_profanity()