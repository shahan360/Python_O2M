"""Created a dictionry with the name user"""

user = {
    "name":"john",
    "sex":"M",
    "age":22
}

print("john" in user.items()) # checks if the value "john" is in user dictionary keys or not
print("sex" in user) # checks if the value "sex" is in user dictionary keys or not

print("john" in user.values()) # checks if the value "john" is in user dictionary values or not
print("sex" in user.keys()) # checks if the value "sex" is in user dictionary keys or not

print(user.items()) # returns a list containing a tuple for each key value pair

print(user.clear()) # clears the dictionary
print(user) # returns the empty "user" dictionary

user2 = {
    "name":"Ramy",
    "sex":"M",
    "age":47
    }

print(user2.pop("age"))
print(user2) # removes the key value pair from the dictionary

print(user2.update({"sex":"F"}))
print(user2) # updates the dictionary with the new key value pair

print(user2.update({"size":32}))
print(user2) # updates the dictionary with the new key value pair

print(user2.popitem()) # it randomly pops an item
print(user2) # removes the key value pair from the dictionary

print(user2.keys())
print(user2.values())

user3 = {
    'age':45,
    'username':"john",
    'weapons':["sword", "gun"],
    'is_active':True,
    'clan':"India"
    }

user3['weapons'].append('shield')
user3["weapons"] = user3["weapons"]+["pistol"]
print(user3)