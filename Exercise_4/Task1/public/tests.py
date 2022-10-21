#!/usr/bin/env python3

from unittest import TestCase
from script import fac, fac_iterative


class PublicTestSuite(TestCase):

    def test1(self):
         self.assertEqual(120, fac(5))
    
    def test1_iterative(self):
        self.assertEqual(120, fac_iterative(5))

t = PublicTestSuite()
t.test1()
t.test1_iterative()

