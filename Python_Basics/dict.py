my_dict = {
    'a' : [1,2,3],
    'b' : "hello",
    'c' : True
    }

my_list = [
    {
    'a' : [1,2,3],
    'b' : "hello",
    'c' : True
    },
    {
    'a' : [4,5,6],
    'b' : "bye",
    'c' : False
    }
    ]

print(my_dict["a"])
print(my_dict["a"][1])
print(my_list[1]["a"][2])