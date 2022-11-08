#!/usr/bin/env python3

from unittest import TestCase
from script import analyze

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".


class PublicTestSuite(TestCase):

    def test_1(self):
        actual = analyze(["hi #weekend",
                          "good morning #zurich #limmat",
                          "spend my #weekend in #zurich",
                          "#zurich <3"])
        expected = {'weekend': 2, 'zurich': 3, 'limmat': 1}
        self.assertEqual(expected, actual)

    def test_hashtag_with_non_ascii(self):
        actual = analyze(["hi #week.end",
                          "good morning #zurich #limmat",
                          "spend my #weekend in #zurich",
                          "#zurich <3"])
        expected = {'week':1, 'weekend': 1, 'zurich': 3, 'limmat': 1}
        self.assertEqual(expected, actual)
    
    def test_two_consecutive_hashtags(self):
        actual = analyze(["hi ##weekend",
                          "good morning #zurich #limmat",
                          "spend my #weekend in #zurich",
                          "#zurich <3"])
        expected = {'weekend': 2, 'zurich': 3, 'limmat': 1}
        self.assertEqual(expected, actual)

    def test_with_one_char(self):
        actual = analyze(["hi #weekend #w",
                          "good morning #zurich #limmat",
                          "spend my #weekend in #zurich",
                          "#zurich <3"])
        expected = {'weekend': 2, 'w':1, 'zurich': 3, 'limmat': 1}
        self.assertEqual(expected, actual)

    # Hint: Hashtag extraction is not correct for '.#c.'.
    def test_hint1(self):
        actual = analyze([".#c."])
        expected = {'c':1}
        self.assertEqual(expected, actual)
    
    def test_only_hashtag_in_word(self):
        actual = analyze(["#"])
        expected = {}
        self.assertEqual(expected, actual)
    
        

t = PublicTestSuite()
t.test_1()
t.test_hashtag_with_non_ascii()
t.test_two_consecutive_hashtags()
t.test_with_one_char()
t.test_hint1()
t.test_only_hashtag_in_word()