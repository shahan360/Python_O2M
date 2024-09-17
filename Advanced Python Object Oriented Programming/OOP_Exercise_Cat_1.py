# exercise cats everywhere

# Given the below class Cat:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 1 instantiate the Cat object with 3 cats.
cat1 = Cat('cat1',5)
cat2 = Cat('cat2',6)
cat3 = Cat('cat3',7)

# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.') # Here we are passing attribute age of multiple cat objects as arguments