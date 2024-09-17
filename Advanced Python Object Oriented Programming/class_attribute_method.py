class PlayerCharacter:
    membership = True # Class object attribute, its an attribute of PlayerCharacter. It is a static attribute
    def __init__(self, name, age):
        if self.membership: # or we can write: 'if PlayerCharacter.membership :'
            self.name = name # these are dynamic attribute
            self.age = age
    
    def bless(self):
        print(f"Bless me {self.name}")
        # print(f"run {PlayerCharacter.name}") # we cannot do this

player1 = PlayerCharacter("Ram",22)
player2 = PlayerCharacter("Jesus", 25)

print(player1.name)
print(player1.membership) # each of the class instance can access the class object attribute
print(player1.bless())

print(player2.name)
print(player2.membership)
print(player2.bless())