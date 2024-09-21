def my_decorator(func):  # 'my_decorator' is a higher-order function (decorator) that takes another function 'func' as an argument.
    def wrap_func(*args, **kwargs):  # 'wrap_func' is a wrapper function that accepts any number of positional (*args) and keyword (**kwargs) arguments.
        func(*args, **kwargs)  # The original function 'func' is called with its arguments.
    return wrap_func  # The decorator returns the wrapped function with the same signature as the original function.

@my_decorator  # The '@my_decorator' syntax applies 'my_decorator' to the 'hello' function. It's syntactic sugar for hello = my_decorator(hello).
def hello(name, age):  # 'hello' function takes two arguments: name and age.
    print(f"Hello, {name}! You are {age} years old.")  # This prints a greeting message including the name and age.

@my_decorator  # The '@my_decorator' syntax applies 'my_decorator' to the 'logged_in' function.
def logged_in(username):  # 'logged_in' function takes one argument: username.
    print(f"{username} is logged in.")  # This prints a message that the specified user is logged in.

hello("Captain America", 105)  # Calls the 'hello' function with the arguments "Captain America" and 105.
logged_in("Steve Rogers")  # Calls the 'logged_in' function with the argument "Steve Rogers".

# Using the decorator would be the same as doing the following manually:
# my_decorator(hello)("Captain America", 105)  # This wraps 'hello' in 'my_decorator' and calls it with the arguments.
# my_decorator(logged_in)("Steve Rogers")  # This wraps 'logged_in' in 'my_decorator' and calls it with the argument.
