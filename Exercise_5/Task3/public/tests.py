from unittest import TestCase
import script

class PrivateTestSuite(TestCase):

    # If this test passes, that does not mean that you will get any points.
    # The grading system uses different, more exhaustive tests.

    # Feel free to extend the class with your own test cases,
    # which will then also be executed in every "Test & Run".

    # Check if the return type is dict
    def test_return_type_reverse_index(self):
        dataset = [
            "Hello world",
            "This is the WORLD",
            "hello again"
        ]           
        actual = script.reverse_index(dataset)
        message = "@@Expected return type is dict but {} is returned !@@".format(type(actual).__name__)
        self.assertIsInstance(actual,dict,message)

    def test_input1(self):
        dataset = [
            "Hello world",
            "This is the WORLD",
            "hello again"
        ]
        actual = script.reverse_index(dataset)
        assert(actual == {
            'hello': [0, 2],
            'world': [0, 1],
            'this': [1],
            'is': [1],
            'the': [1],
            'again':[2]})

t = PrivateTestSuite()
t.test_return_type_reverse_index()
t.test_input1()

