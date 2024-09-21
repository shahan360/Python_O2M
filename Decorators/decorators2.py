def hello(func):  # 'hello' is a higher-order function that takes another function 'func' as an argument.
    func()  # The passed function (func) is executed here.

def greet():  # 'greet' is a simple function that prints a message.
    print("Hello, Marvel Cinematic Universe!")

# Call 'hello' and pass 'greet' as an argument.
# This demonstrates that functions can be passed as arguments to other functions.
hello(greet)  # This calls the 'hello' function with 'greet' as an argument, which results in 'greet()' being executed.

# This example shows that functions can be treated as first-class citizens in Python, 
# meaning they can be passed around as variables and used as arguments to other functions.
