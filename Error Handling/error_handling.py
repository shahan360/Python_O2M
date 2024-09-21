while True:  # Infinite loop to keep asking for the user's age until valid input is provided.
    try:
        # Prompt the user to enter their age, and attempt to convert the input to an integer.
        age = int(input("Enter your age: "))

        # Calculate age in "dog years" by dividing 10 by the entered age.
        # This line may raise a ZeroDivisionError if age is 0.
        age_in_dogs_year = 10 / age

    except ZeroDivisionError:  # This block handles division by zero errors.
        # If the user enters 0, this message is printed, and the loop continues.
        print("Please enter a valid age. Age cannot be 0.")
        continue  # Skip the rest of the loop and restart the next iteration.

    except ValueError:  # This block handles invalid input (non-integer).
        # If the user enters a non-numeric value, this message is printed, and the loop exits.
        print("Please enter a valid age. Age cannot be a string.")
        break  # Exit the loop on invalid (non-integer) input.

    else:  # This block executes if no exceptions are raised.
        # If the age input is valid, print a thank you message and the age.
        print(f"Thank you, and your age is {age}.")
        break  # Exit the loop after successfully processing valid input.

    finally:  # This block always executes, regardless of any exception being raised.
        # This prints every time the loop runs, mimicking Thanos's famous line.
        print("I am finally, I'm Thanos. Dread it, run from it, finally still arrives.")

    # This line runs if no `continue` or `break` occurs within the loop body.
    print("Where are the infinity stones???")
