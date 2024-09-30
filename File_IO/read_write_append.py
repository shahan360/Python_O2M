# Open the file 'happy.txt' in append mode ('a')
# If the file doesn't exist, it will be created.
# If it does exist, new content will be added to the end of the file.
with open("happy/happy.txt", mode='a') as my_file:
    # Write the string "I am HAPPY!" to the file.
    # The write() method returns the number of characters written, which is stored in 'text'.
    text = my_file.write("I am HAPPY!")
    
    # Print the number of characters written to the file
    print(text)  # Output will be the number of letters written, i.e., 11 in this case.

# Open the same file 'happy.txt' in read mode ('r') to check the content.
with open("happy/happy.txt", mode='r') as my_file:
    # Read and print the entire content of the file.
    # This will include the newly appended text along with any previous content.
    print(my_file.read())  # Output will be the content of the file.

'''
File Mode Explanations:

1. mode = 'w'  : Creates a new file or replaces an existing file with the same name, writing new content.
2. mode = 'r'  : Opens the file for reading. If the file doesn't exist, it will raise a FileNotFoundError.
3. mode = 'r+' : Opens the file for both reading and writing. Writing starts from position 0, potentially overwriting some existing content.
4. mode = 'a'  : Opens the file for appending. New content is added to the end of the file without altering the existing content.
                 If the file doesn't exist, a new file will be created.

Note:
- If no mode is specified, the default mode is 'r' (read).
- Using the 'with' statement ensures that the file is closed automatically after the block of code is executed, 
  so you don't need to call `my_file.close()` manually.
'''
