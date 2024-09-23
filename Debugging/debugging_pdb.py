# Importing the Python debugger module
import pdb

# Define a function to add two numbers
def add(n1, n2):
    # This function returns the sum of n1 and n2
    return n1 + n2

# Start the debugger, setting a breakpoint at this line
pdb.set_trace()

# Calling the add function with an integer and a string, which will cause a TypeError
# Since you cannot add a string ('four') to an integer (4), the debugger will help us inspect the issue.
add(4, 'four')

'''
Useful pdb commands for debugging:

a          : Prints the argument list of the current function.
step       : Executes the current line of code and pauses at the next step.
help       : Lists all available commands in the debugger.
help <cmd> : Shows detailed help for a specific command.
continue   : Continues running the program until it encounters another breakpoint or an error.
w          : Displays the previous, current, and next lines of code.
next       : Executes the next line of code in the current function.

Note: 
- You can modify variable values during debugging.
- Typing a variable name in the debugger will print its current value.
'''
