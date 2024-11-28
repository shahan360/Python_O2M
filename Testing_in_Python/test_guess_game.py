# Importing the required modules
import unittest  # The unittest module is used for writing test cases.
import guess_game  # Assuming guess_game is a module that contains the game logic.

class TestGame(unittest.TestCase):
    """
    TestGame is a test class derived from unittest.TestCase, which is used to
    test the 'run_guess' function in the 'guess_game' module.
    
    The function 'run_guess' takes two arguments: the guessed number and the correct number,
    and returns True if the guess is correct, otherwise False.
    """

    def test_game(self):
        """
        Test Case 1:
        This test checks if the 'run_guess' function returns True
        when the guessed number is equal to the correct number (5).
        """
        result = guess_game.run_guess(5, 5)
        self.assertTrue(result)  # Expecting True because the guess is correct.

    def test_game2(self):
        """
        Test Case 2:
        This test checks if the 'run_guess' function returns False
        when the guessed number is less than the correct number (0 vs 5).
        """
        result = guess_game.run_guess(0, 5)
        self.assertFalse(result)  # Expecting False because the guess is incorrect.

    def test_game3(self):
        """
        Test Case 3:
        This test checks if the 'run_guess' function returns False
        when the guessed number is still less than the correct number (1 vs 5).
        """
        result = guess_game.run_guess(1, 5)
        self.assertFalse(result)  # Expecting False because the guess is incorrect.

# Running the tests if this file is executed directly.
if __name__ == '__main__':
    unittest.main()

