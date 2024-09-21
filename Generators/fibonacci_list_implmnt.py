# Function to generate Fibonacci sequence up to 'num' terms
def fib(num):
    a = 0  # Initialize first number of the Fibonacci sequence
    b = 1  # Initialize second number of the Fibonacci sequence
    li = []  # List to store the Fibonacci sequence

    # Loop to generate Fibonacci sequence up to 'num' terms
    for i in range(num):
        li.append(a)  # Append the current number (a) to the list
        temp = a  # Temporarily store the value of 'a'
        a = b  # Assign the value of 'b' to 'a' (next number in the sequence)
        b = temp + b  # Update 'b' to be the sum of previous two numbers

    print(li)  # Print the generated Fibonacci sequence

# Input from user to specify the number of terms in the Fibonacci sequence
num = int(input("Enter a number: "))

# Call the Fibonacci function with the input number
fib(num)
