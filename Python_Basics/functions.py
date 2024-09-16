# Positional Parameters
def say_hello(name, age):
    print(f'Hi {name}, your age is {age}')
    
# Default Parameters
def say_hello2(name="Brian", age=25):
    print(f'Hi {name}, your age is {age}')

# Positional Arguments
say_hello("Rajeev", 27)

# Default Arguments
say_hello2()
say_hello2("Rajeev")

# Key Arguments
say_hello(age = 89, name = "Joseph")