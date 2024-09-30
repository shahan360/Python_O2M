# Import the unittest module for creating unit tests
import unittest
# Import the 'script' module which contains the function to be tested
import script

# Define a class 'TestMain' which inherits from 'unittest.TestCase'
# This class contains test cases to validate the functionality of the 'add' function in 'script'
class TestMain(unittest.TestCase):  
    """
    Test class for testing the 'add' function in the 'script' module.
    Inherits from unittest.TestCase to utilize built-in testing methods.
    """
    
    def test_add(self):
        """
        Test case to verify the 'add' function when passing a valid integer.
        It checks if adding 5 to the input 10 gives the expected result 15.
        """
        test_param = 10  # Input parameter for the 'add' function
        result = script.add(test_param)  # Call the 'add' function from 'script' with the test parameter
        self.assertEqual(result, 15)  # Check if the result equals the expected output (15)
    
    def test_add2(self):
        """
        Test case to verify the 'add' function when passing an invalid input (string).
        It checks if the function returns a ValueError for invalid input.
        """
        test_param = 'random string'  # Invalid input parameter (string) for the 'add' function
        result = script.add(test_param)  # Call the 'add' function from 'script' with the test parameter
        self.assertTrue(isinstance(result, ValueError))  # Check if the result is a ValueError

# Entry point for running the unit tests.
# This block ensures that the tests are run only when the script is executed directly, not when imported.
if __name__ == '__main__':
    unittest.main()  # Run all test cases
