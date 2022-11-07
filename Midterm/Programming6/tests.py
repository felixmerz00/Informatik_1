from unittest import TestCase
import script

class PublicTestSuite(TestCase):

    def test1(self):
        actual = True
        expected = True
        self.assertEqual(expected, actual)
        print("Test 1 passed.")
    
    def test2(self):
        actual = True
        expected = True
        self.assertEqual(expected, actual)
        print("Test 2 passed.")

    def test3(self):
        actual = True
        expected = True
        self.assertEqual(expected, actual)
        print("Test 3 passed.")

    def test4(self):
        actual = True
        expected = True
        self.assertEqual(expected, actual)
        print("Test 4 passed.")

t = PublicTestSuite()
# t.test1()
# t.test2()
# t.test3()
# t.test4()