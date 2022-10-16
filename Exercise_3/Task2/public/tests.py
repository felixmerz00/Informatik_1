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

    def test_return_types(self):
        actual = script.is_valid()
        m = "The is_valid function should return a bool!"
        self.assertTrue(isinstance(actual, bool), m)

    def test_length(self):
        script.pwd = "HelloHe"  # 7 chars
        res = script.is_valid()
        self.assertEqual(res, False)

        script.pwd = "HEll00++"   # 8 chars
        res = script.is_valid()
        self.assertEqual(res, True)

        script.pwd = "HEll00++loHelloH"    # 16 chars
        res = script.is_valid()
        self.assertEqual(res, True)

        script.pwd = "HEll00++loHelloHe"    # 17 chars
        res = script.is_valid()
        self.assertEqual(res, False)
    
    def test_correct_characters(self):
        script.pwd = "HEll00++löHällüH"    # Correct symbols
        res = script.is_valid()
        self.assertEqual(res, True)
        
        script.pwd = "HEll00+.loHelloH"    # False symbol "."
        res = script.is_valid()
        self.assertEqual(res, False)

        script.pwd = "HEll00++=oHelloH"    # False symbol "="
        res = script.is_valid()
        self.assertEqual(res, False)

    def test_correct_number_of_chars(self):
        script.pwd = "ÖÄül00++"    # Correct symbols
        res = script.is_valid()
        self.assertEqual(res, True)

        script.pwd = "ÖÄTl00++"    # Only one lower case char
        res = script.is_valid()
        self.assertEqual(res, False)

        script.pwd = "Öüül00++"    # Only one upper case char
        res = script.is_valid()
        self.assertEqual(res, False)

        script.pwd = "ÖÄül0e++"    # Only one digit
        res = script.is_valid()
        self.assertEqual(res, False)
        
        script.pwd = "ÖÄül00p+"    # Only one special symbol
        res = script.is_valid()
        self.assertEqual(res, False)

    def test_submission_feedback(self):
        script.pwd = "xW+5xW+5"
        res = script.is_valid()
        self.assertEqual(res, True)



t = PublicTestSuite()
t.test_return_types()
t.test_length()
t.test_correct_characters()
t.test_correct_number_of_chars()
t.test_submission_feedback()