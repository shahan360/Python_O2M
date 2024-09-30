my_file = open('/Users/shahan/Coding_Projects/Python_O2M/File_IO/test.txt') # Give the complete file path
print(my_file)
print(my_file.read())

print(my_file.read()) # it won't be printing anything. because the cursor is at the end of the file.

print("Seek 0")
my_file.seek(0) # we reset the cursor to the initial position.

print(my_file.read()) # and so we can now read the file from the initial position till end.

print("Seek 0")
my_file.seek(0)

print(my_file.readline()) # reads a line and stop the cursor
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

print("Seek 0")
my_file.seek(0)

print(my_file.readlines()) # reads all the lines and store them in a list.
print(my_file.readlines()) # it will be empty because the cursor is at the end of the file

my_file.close() # it is important to close the file after reading it.