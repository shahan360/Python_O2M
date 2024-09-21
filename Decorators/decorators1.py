def hello():
    print("Hello! Marvel Cinematic Universe")

# Assigning the 'hello' function to the variable 'greet'
greet = hello

# Deleting the 'hello' function reference, but 'greet' still points to the same function object
del hello

# The function is not deleted from memory, only the name 'hello' is removed from the current namespace.
# The 'greet' variable still holds the reference to the original 'hello' function.

# (hello()  # this will give an error, because 'hello' has been deleted
print(greet)  # This will print the memory reference of the 'greet' function
greet()  # This will call the function via 'greet', still functioning as expected
