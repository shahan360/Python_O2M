# Function to generate Fibonacci sequence
def fib(num):
    # Initialize the first two numbers of the Fibonacci sequence
    a = 0
    b = 1
    
    # Loop through the sequence 'num' times
    for i in range(num):
        # Yield the current value of 'a' (the next number in the sequence)
        yield a
        
        # Temporarily store the current value of 'a'
        temp = a
        
        # Set 'a' to the next number in the sequence (the current value of 'b')
        a = b
        
        # Update 'b' to be the sum of the previous two numbers
        b = temp + b

# Prompt the user to enter the number of Fibonacci numbers to generate
num = int(input("Enter a number: "))

# Loop through the Fibonacci generator and print each value
for i in fib(num):
    print(i)
