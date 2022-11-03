#!/usr/bin/env python3

from unittest import TestCase
import script

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".

class PublicTestSuite(TestCase):

    def test_1(self):
        script.wa_nrs = []
        
        actual = script.get_possible_nrs("077342119")
        self.assertEqual([], actual, "script should not find any number on an empty wa_nrs list")

    def test_2(self):
        script.wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]
        actual = script.get_possible_nrs("076432165")
        expected = ["0764320165"]
        self.assertEqual(expected, actual)

    # Hint: The expected phone numbers are ['0779266313', '0789266313', '0792566313', '0792646313', '0792663113', '0792663130', '0792663213', '0792663313', '0792696313', '0796266313'] but ['0779266313', '0789266313', '0792566313', '0792646313', '0792663113', '0792663113', '0792663130', '0792663213', '0792663313', '0792663313', '0792696313', '0796266313'] have been found.

t = PublicTestSuite()
t.test_1()
t.test_2()
