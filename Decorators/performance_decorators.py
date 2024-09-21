from time import time  # Import the 'time' function to measure execution time.

# Define a decorator 'performance' to measure the time taken by a function.
def performance(fn):  
    def wrap_fn(*args, **kwargs):  # This is a wrapper function that accepts any number of arguments (*args) and keyword arguments (**kwargs).
        t1 = time()  # Record the start time before executing the function.
        fn(*args, **kwargs)  # Execute the original function (fn) with its arguments.
        t2 = time()  # Record the end time after the function finishes executing.
        print(f"Time taken: {t2 - t1} seconds.")  # Calculate and print the time difference (execution time).
    return wrap_fn  # Return the wrapper function.

# Use the 'performance' decorator to wrap 'long_fn' and measure its execution time.
@performance
def long_fn():  
    # A simple function that runs a loop 1,000,000 times, doing a multiplication operation on each iteration.
    for i in range(1000000):
        i * 5  # Multiplying 'i' by 5 (though the result is not used).

# Call 'long_fn', which will now be timed due to the 'performance' decorator.
long_fn()
