#!/usr/bin/env python3
from unittest import TestCase
from script import evolve


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class EvolveTestSuite(TestCase):

    def test_glider(self):
        world = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        expected = ((
                        "--------------",
                        "| ###        |",
                        "| #          |",
                        "|  #         |",
                        "|            |",
                        "|            |",
                        "--------------"
                    ), 5)
        actual = evolve(world, 4)
        self.assertEqual(actual, expected)

    def test_world_is_tuple_of_strings(self):
        with self.assertRaises(Warning):
            evolve((5, 5, 3), 5)

    def test_wrong_character1(self):
        world = (
            "--X-----------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_wrong_character2(self):
        world = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #   L     |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_wrong_character3(self):
        world = (
            "--------------",
            "|    -       |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_wrong_character4(self):
        world = (
            "--------------",
            "|            |",
            "|  ###       |",
            "|  #       | |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_wrong_character5(self):
        world = (
            "--------------",
            "             |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_different_length1(self):
        world = (
            "---------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_different_length2(self):
        world = (
            "--------------",
            "|            |",
            "|  ##      |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_different_length3(self):
        world = (
            "---------------",
            "|            |",
            "|  ###  #     |",
            "|  #         |",
            "|   #        |",
            "|          #  |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_different_length4(self):
        world = (
            "---------------",
            "|            |",
            "|  ###       |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_smaller_than_3_by_3(self):
        world = (
            "--",
            "||",
            "--"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_steps_positive_int1(self):
        world = (
            "--------------",
            "|            |",
            "|  ##        |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, -3)

    def test_steps_positive_int2(self):
        world = (
            "--------------",
            "|            |",
            "|  ##        |",
            "|  #         |",
            "|   #        |",
            "|            |",
            "--------------"
        )
        with self.assertRaises(Warning):
            evolve(world, "5")

    def test_empty_world1(self):
        world = ()
        with self.assertRaises(Warning):
            evolve(world, "5")

    def test_empty_world2(self):
        world = (
            "-----",
            "-----"
        )
        with self.assertRaises(Warning):
            evolve(world, 5)

    def test_wrong_input(self):
        world = (
            "---",
            "|X|",
            "---"
        )
        with self.assertRaises(Warning):
            evolve(world, "5")

t = EvolveTestSuite()
t.test_glider()
t.test_world_is_tuple_of_strings()
t.test_wrong_character1()
t.test_wrong_character2()
t.test_wrong_character3()
t.test_wrong_character4()
t.test_wrong_character5()
t.test_different_length1()
t.test_different_length2()
t.test_different_length3()
t.test_different_length4()
t.test_smaller_than_3_by_3()
t.test_steps_positive_int1()
t.test_steps_positive_int2()
t.test_empty_world1()
t.test_empty_world2()
t.test_wrong_input()