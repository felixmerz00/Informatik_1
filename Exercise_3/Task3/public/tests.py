#!/usr/bin/env python3
from unittest import TestCase

import script

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

class PublicTestSuite(TestCase):

    def test_case0(self):
        actual = script.rot_n()
        m = "The rot_n function should return a string!"
        self.assertTrue(isinstance(actual, str), m)
    
    def test_example(self):
        script.plain_text = "a, B, z#!"
        script.shift_by = 1
        actual = script.rot_n()
        expected = "b, C, a#!"
        self.assertEqual(expected, actual)

t = PublicTestSuite()
t.test_case0()
t.test_example()