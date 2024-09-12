user = {
        "name": "john",
        "sex": "M",
        "age": 22
        }

# print(user["height"]) # this will give us error, as height doesn't exit in the dictionary.

print(user.get("height"))

print(user.get("height", 5.6)) # if the key value pair doesn't exit, then it will write the default value.
print(user)

# new way to create a dictionary
user2 = dict(name = "Manav", age = 25)
print(user2)
print(user2["name"])