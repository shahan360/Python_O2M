def my_own_forloop_fn(iterable):
    # Create an iterator from the iterable
    iterator = iter(iterable)
    
    # Infinite loop to mimic the behavior of a for loop
    while True:
        try:
            # Print the iterator object (for demonstration purposes)
            print(iterator)
            
            # Retrieve the next item from the iterator and print it
            print(next(iterator))
        
        # Handle the StopIteration exception when the iterator is exhausted
        except StopIteration:
            # Break the loop when all items are processed
            break

# Call the function with a list of numbers as the iterable
my_own_forloop_fn([1, 2, 3, 4, 5])
