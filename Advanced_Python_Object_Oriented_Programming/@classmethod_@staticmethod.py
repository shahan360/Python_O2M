class PlayerCharacter:
    membership  = True
    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def run(self):
        print(f"run {self.name}")

    @classmethod # we can use this method without instantiating the class
    def adding_things(cls, num1, num2):
        return cls('Greta', num1+num2)

    @staticmethod # same as @classmethod, only thing is we don't pass the class as argument, and hence can't use its attribute
    def adding_things2(num1, num2):
        return num1+num2

player1 = PlayerCharacter.adding_things(4,5)
print(player1.name)
print(player1.age)
print(player1.membership)

print(PlayerCharacter.adding_things2(4,5)) # we don't need to instantiate the class to use this method
print(player1.adding_things2(4,5)) # we can use this method with an instance of the class as well
# print(player2.membership) # gives error
