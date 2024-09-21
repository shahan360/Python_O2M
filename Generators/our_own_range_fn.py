class MyOwnRangeFn():
    # Class-level attribute to keep track of the current number
    current = 0
    
    def __init__(self, first, last):
        """
        Initialize the range function with the first and last values.
        Parameters:
        - first: The starting value of the range
        - last: The end value of the range
        """
        self.first = first  # Start of the range
        self.last = last    # End of the range

    def __iter__(self):
        """
        Return the iterator object itself.
        This makes the class iterable.
        """
        return self

    def __next__(self):
        """
        Return the next number in the range.
        Raises StopIteration when the end of the range is reached.
        """
        print("Say the hehehehe from Green Goblin")  # Sample print statement for demonstration
        # Check if the current value is less than the end value
        if self.current < self.last:
            num = MyOwnRangeFn.current  # Store the current value
            MyOwnRangeFn.current += 1   # Increment the current value for the next iteration
            return num  # Return the current number
        # If the current value exceeds the end value, raise StopIteration to stop the iteration
        raise StopIteration

# Instantiate the custom range generator with a start and end value
gen = MyOwnRangeFn(0, 10)
print(gen)

# Iterate through the generated numbers
for i in gen:
    print(i)

'''
Note:
- Loops (such as for-loops) automatically handle StopIteration exceptions, 
  so they stop gracefully when the iteration is complete.
'''
