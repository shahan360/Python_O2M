# Higher Order Function (HOC) is a function which returns another function, or accepts another function

def greet(func):  # 'greet' is a higher-order function because it takes another function (func) as an argument.
    func()  # The passed function is called within 'greet'.

def greet2():  # 'greet2' is a regular function, not a higher-order function.
    def hello():  # 'hello' is a nested function, but not a higher-order function.
        print("hello!")  # 'hello' prints the string "hello!".
    return hello()  # 'greet2' returns the result of calling 'hello()', but does not return the function itself, so it is not higher-order.

print(greet(greet2))  # 'greet' is called with 'greet2' as an argument, making 'greet' a higher-order function.
    