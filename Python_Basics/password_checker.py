user_name = input("Enter your username:")
password = input("Enter your password:")
password_length = len(password)
hidden_password = '*' * password_length
print(f'Hey {user_name}, your {hidden_password} is of {password_length} characters in length')