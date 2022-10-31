#!/usr/bin/env python3
from unittest import TestCase

import script

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")

class PublicTestSuite(TestCase):
    def test_return_type(self):
        self.assertIn(type(script.hamming_dist(signal_sensor_1, signal_sensor_2)), [str, list])

    def test_get_hamming_dist(self):
        self.assertEqual(script.get_hamming_dist("1", "1"), 0)
        self.assertEqual(script.get_hamming_dist("00101110", "00101110"), 0)
        self.assertEqual(script.get_hamming_dist("1101", "1111"), 1)
        self.assertEqual(script.get_hamming_dist("shift", "tshif"), 5)
    
    def test_empty_signal(self):
        # Both have length 0
        ss1 = {"times": [], "data": []}
        ss2 = ()
        self.assertEqual(script.hamming_dist(ss1, ss2), "Empty signal on at least one of the sensors")
        # They have unequal length
        ss1 = {"times": [0, 1, 2],
                        "data": ["00101110", "11001011", "11110000"]}
        ss2 = ("00101110", "11001001")
        self.assertEqual(script.hamming_dist(ss1, ss2), "Empty signal on at least one of the sensors")

    def test_sensor_defect(self):
        ss1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "0001011"]}
        ss2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
        self.assertEqual(script.hamming_dist(ss1, ss2), "Sensor defect detected")

    def test_example(self):
        ss1 = {"times": [0, 2, 5], "data": ["0010", "1101", "1100"]} 
        ss2 = ("0010", "1111", "0000")
        expected = [("1101", "1111", 1), ("1100", "0000", 2)]
        self.assertEqual(script.hamming_dist(ss1, ss2), expected)


t = PublicTestSuite()
t.test_return_type()
t.test_get_hamming_dist()
t.test_empty_signal()
t.test_sensor_defect()
t.test_example()

        
