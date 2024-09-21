# We can intentionally stop the program by raising our own exceptions.

print("Hello Peter!!!!")  # This prints a greeting message.

# raise TypeError("I'm Dr. Octopus")

# The following line raises a general exception. When raised, the program will stop executing any further code.
raise Exception("How did you do that?")  # Custom message for the exception.

# This line will not be executed because the exception above stops the program.
print("Thanks Peter!!!!")  
