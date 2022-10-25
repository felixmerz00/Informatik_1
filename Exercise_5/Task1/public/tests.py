#!/usr/bin/env python3

from unittest import TestCase
from script import merge

# This test suite does not exhaustively test the
# implementation, a passing "test & run" does not mean that all
# possible cases have been considered. For the grading, an
# extended tests suite will be executed that will cover many
# more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".


class PublicTestSuite(TestCase):

    def test_1(self):
        actual = merge([0, 1, 2], [5, 6])
        expected = [(0, 5), (1, 6), (2, 6)]
        self.assertEqual(expected, actual)
    def test_2(self):
        actual = merge([0, 1, 2], [5, 6, 7])
        expected = [(0, 5), (1, 6), (2, 7)]
        self.assertEqual(expected, actual)

    def test_3(self):
        actual = merge([2, 1, 0], [5, 6])
        expected = [(2, 5), (1, 6), (0, 6)]
        self.assertEqual(expected, actual)
    
    def test_4(self):
        actual = merge([], [2, 3])
        self.assertEqual([], actual)

t = PublicTestSuite()
t.test_1()
t.test_2()
t.test_3()
t.test_4()