# Importing the necessary modules for testing
import unittest  # The built-in unit testing framework
import script    # Importing the script file where the 'add' function is defined

# Defining a test class that inherits from unittest.TestCase
class TestMain(unittest.TestCase):
    """
    TestMain class:
    This class contains unit tests for the 'add' function from the 'script' module.
    It inherits from 'unittest.TestCase', which provides several testing features.
    """
    
    def setUp(self):
        """
        setUp method:
        This method is called before each test method execution. 
        It is generally used to set up any initial variables or state before running the tests.
        """
        print("Starting a method/test: ")

    def test_add(self):
        """
        test_add method:
        This test checks if the 'add' function correctly adds 5 to a given integer input.
        """
        test_param = 10  # The input parameter for the test
        result = script.add(test_param)  # Call the 'add' function from the 'script' module
        self.assertEqual(result, 15)  # Asserting if the result is equal to 15 (10 + 5)

    def test_add2(self):
        """
        test_add2 method:
        This test checks if the 'add' function correctly handles non-integer input (in this case, a string) 
        and raises a ValueError.
        """
        test_param = 'random string'  # The input parameter for the test (a string in this case)
        result = script.add(test_param)  # Call the 'add' function from the 'script' module
        # Asserting if the function raises a ValueError for the given string input
        self.assertTrue(isinstance(result, ValueError))

    def tearDown(self):
        """
        tearDown method:
        This method is called after every test method execution. 
        It is generally used for cleaning up or resetting variables after a test.
        """
        print("Cleaning up....")

# A sample class outside the test structure (doesn't serve a purpose in testing)
class A:
    print("\nClass A")

# Ensures the test cases are executed when this script is run directly
if __name__ == '__main__':
    unittest.main()  # This will run all the test cases defined in the TestMain class

# Another sample class, outside the test structure (also not relevant to the tests)
class B:
    print("\nClass B")
