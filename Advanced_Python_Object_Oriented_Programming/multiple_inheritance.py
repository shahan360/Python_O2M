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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"{self.name} is attacking with {self.arrows} arrows.")

    def check_arrows(self):
        print(f"{self.arrows} arrows left.")

class HybridAttacker(Wizard, Archer): # notice the order, in that order only it will give preference
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

doombot = HybridAttacker("Viktor Von Doom", 100, 110)
doombot.attack()

print(doombot.name)
print(doombot.power)
print(doombot.arrows)

doombot.check_arrows()
doombot.sign_in_check()