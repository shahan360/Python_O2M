import re  # Import the regular expression module for pattern matching

# Define a regular expression pattern for validating email addresses
# The pattern checks for:
# - One or more alphanumeric characters (including '.', '_', '-', and '+') before the '@' symbol
# - One or more alphanumeric characters (including '-') after the '@' symbol
# - A period followed by one or more alphanumeric characters (including '-', '.', and letters) for the domain
email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

# Check if the provided email matches the defined pattern
check_email = email_pattern.fullmatch('tonystarkISdrdoom1111@starkdoom.com')

# Define a regular expression pattern for validating passwords
# The pattern checks for:
# - At least 8 characters long
# - Can contain alphanumeric characters and the special characters '@', '#', and '$'
password_pattern = re.compile(r"([a-zA-Z0-9@#$%]{8,}$)")

# Check if the provided password matches the defined pattern
check_password = password_pattern.fullmatch('P@ssw0rd')

# Validate the email and password
if check_email and check_password:
    # If both the email and password are valid, print a success message
    print('Valid email and password')
else:
    # If either the email or password is invalid, print an error message
    print('Invalid email and password. Please try again.') 

'''
Notes:
- The email pattern allows for a variety of characters in both the local and domain parts.
- The password pattern enforces a minimum length of 8 characters and allows specific special characters.
- It is important to ensure that both the email and password meet their respective validation criteria.
'''
