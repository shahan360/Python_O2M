class User():
    def sign_in_check(self):
        print("User is logged in.")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")

class Archer(User):
    pass

wizard1 = Wizard("John", 50)

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(wizard1, Archer))

'''
By default every class is a subclass of 'object' class, hence when we type 'instance.' (object_name dot), we get all those
defualt methods suggestions from the IDE.
'''