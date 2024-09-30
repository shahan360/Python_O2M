# Open the file 'happy.txt' located in the 'happy' directory in append mode ('a').
# If the file does not exist, it will be created.
with open("./happy/happy.txt", mode='a') as my_file:
    # Write the string "I am HAPPY!" to the file.
    # The write() method returns the number of characters written, which is stored in 'text'.
    text = my_file.write("I am HAPPY!")
    
    # Print the number of characters written to the file.
    print(text)  # Output will be the number of letters written, which is 11.

# Open the same file 'happy.txt' located in a different path in read mode ('r') to check its content.
with open("/Users/shahan/Coding_Projects/Python_O2M/File_IO/happy/happy.txt", mode='r') as my_file:
    # Read and print the entire content of the file.
    # This will include the newly appended text along with any previous content.
    print(my_file.read())  # Output will be the content of the file.

'''
Path Explanation:

1. We can specify either an absolute path or a relative path to access files.
2. Relative paths are based on the current working directory:
   - '../' means go back one directory.
   - './' means start from the current directory.
3. Absolute paths provide the complete path from the root of the file system, ensuring the file can be accessed from any location.

Using pathlib module:
- For cross-platform compatibility (Windows, Linux, macOS), the pathlib module can be used.
- This module allows for a more consistent way of handling file paths, making the code portable across different operating systems.
'''
