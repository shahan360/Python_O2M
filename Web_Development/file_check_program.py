import os

file_path = '/Users/shahan/Coding_Projects/Python_O2M/Web_Development/web_server/server.py'
if os.path.isfile(file_path):
    print("File exists.")
else:
    print("File does not exist.")