# Define a custom generator function that behaves similarly to Python's built-in range() function
def generator_fn(num):
    # This print statement will execute only once when the generator is initialized
    print("Generator initialized")
    
    # Use a for loop to iterate through a range of numbers from 0 to num - 1
    for i in range(num):
        # This will print each time before yielding a value
        print("Before yield")
        
        # The yield statement pauses the function and returns control to the caller with the value i * 2
        yield i * 2
        
        # This will execute after the yield when the next() function is called again
        print("After yield")

# Initialize the generator with a range of 3
g = generator_fn(3)

# Print the generator object, which won't run the generator function yet
print(g)

# Calling next() will execute the function up to the first yield and return the yielded value
print(next(g))  # Outputs 0 (0 * 2)

# Calling next() again will continue from where the function was paused
print(next(g))  # Outputs 2 (1 * 2)

# Calling next() again will continue from the previous pause
print(next(g))  # Outputs 4 (2 * 2)

# Uncommenting the following line will raise StopIteration since the generator has no more values
# print(next(g))  # This would raise StopIteration error

# The generator object remains unchanged after exhaustion
print(g)

# Iterate through the generator returned by generator_fn(5) using a for loop
for item in generator_fn(5):
    print(item)  # Prints 0, 2, 4, 6, 8 (each value of i * 2)

# Explanation:
# When a generator is called, it pauses the function execution at 'yield' and returns the value.
# It resumes the function's execution from where it left off when 'next()' or iteration happens.

'''
'yield' is a special keyword that pauses the function and resumes execution upon the next() call.
If 'yield' is present inside a function, Python recognizes it as a generator function, and it won't
execute until it is iterated over or next() is called. It doesn't store all values in memory but 
yields them one by one, which is memory-efficient.
'''
