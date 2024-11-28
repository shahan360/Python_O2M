try:
    # Prompt the user for their age and convert the input to an integer.
    age = int(input("age: "))
    
    # Calculate the value of age as 10 divided by the user input.
    age = 10 / age
    
    # Raise a ValueError with a custom message to indicate an intentional program termination.
    raise ValueError("Ending the program")
    # The line below is commented out; it would raise a general Exception with the message "quit".
    # raise Exception("quit")

# Handle the ValueError that might occur during input or calculation.
except ValueError:
    # Print a message prompting the user to enter a valid number.
    print("Please enter a number.")
