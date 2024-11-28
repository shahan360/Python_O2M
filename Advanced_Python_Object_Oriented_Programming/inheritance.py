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
archer1 = Archer()

print(wizard1.sign_in_check())
print(wizard1.attack())

print(archer1.sign_in_check())