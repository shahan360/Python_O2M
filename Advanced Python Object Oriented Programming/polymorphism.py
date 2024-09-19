class User():
    def sign_in_check(self):
        print("User is logged in.")

    def attack(self):
        print("Do nothing.")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self) # Just a way to use parent class method.
        print(f"{self.name} is attacking with {self.power} power.")

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"{self.name} is attacking with {self.arrows} arrows.")

wizard1 = Wizard("Dr. Strange", 55)
archer1 = Archer("Hawkeye", 100)

wizard1.attack()
archer1.attack()
# notice that these two instances are executing the child class method and not the parent class method.

'''
This is polymorphism.
Even though we are using the same function, it is giving different output based on the object.
'''