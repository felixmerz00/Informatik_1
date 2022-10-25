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
        actual = script.sieve_of_eratosthenes()
        m = "The sieve_of_eratosthenes function should return a list!"
        self.assertTrue(isinstance(actual, list), m)
    
    def test_case1(self):
        script.n = 2
        actual = script.sieve_of_eratosthenes()
        expected = [2]
        self.assertEqual(expected, actual)
        
            
    def test_case2(self):
        script.n = 1
        actual = script.sieve_of_eratosthenes()
        expected = ["empty"]
        self.assertEqual(expected, actual)

    def test_case3(self):
        script.n = 3
        self.assertEqual([2,3], script.sieve_of_eratosthenes())
        script.n = 4
        self.assertEqual([2,3], script.sieve_of_eratosthenes())
        script.n = 5
        self.assertEqual([2,3,5], script.sieve_of_eratosthenes())
        script.n = 6
        self.assertEqual([2,3,5], script.sieve_of_eratosthenes())
        script.n = 7
        self.assertEqual([2,3,5,7], script.sieve_of_eratosthenes())

t = PublicTestSuite()
t.test_case0()
t.test_case1()
t.test_case2()
t.test_case3()
