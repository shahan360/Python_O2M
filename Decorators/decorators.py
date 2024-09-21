def my_decorator(func):  # 'my_decorator' is a higher-order function (decorator) that takes another function 'func' as an argument.
    def wrap_func():  # 'wrap_func' is a nested function that wraps the behavior of the original function 'func'.
        print("*********")  # This is additional behavior that will execute before the original function.
        func()  # The original function 'func' is called here.
        print("*********")  # This is additional behavior that will execute after the original function.
    return wrap_func  # The decorator returns the wrapped function (with the additional behavior).

@my_decorator  # The '@my_decorator' syntax applies 'my_decorator' to the 'hello' function. It's syntactic sugar for hello = my_decorator(hello).
def hello():  # 'hello' is the original function that will be passed to 'my_decorator'.
    print("hello!")  # This is the original behavior of the 'hello' function.

hello()  # This calls the wrapped version of 'hello', which will first execute the additional behavior from 'wrap_func' (before and after the original function).

# Using the decorator is the same as doing the following manually:
# my_decorator(hello)()  # Here, 'my_decorator(hello)' returns 'wrap_func', and 'wrap_func()' is called to execute the wrapped version of 'hello'.
