import requests
import hashlib
import sys

def request_api_data(query_char):
    """
    Requests data from the Pwned Passwords API using the first 5 characters of the SHA-1 hash.

    Args:
        query_char (str): The first 5 characters of the SHA-1 hash of the password.

    Returns:
        Response object: The response from the API containing the hashed password data.

    Raises:
        RuntimeError: If the API response status code is not 200 (indicating an error).
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    
    return res

def get_password_leaks_count(hashes, hash_to_check):
    """
    Parses the API response to count occurrences of the specified hashed password.

    Args:
        hashes (Response object): The response from the Pwned Passwords API containing hashed passwords.
        hash_to_check (str): The tail of the SHA-1 hash that we want to check.

    Returns:
        int: The number of times the specified hashed password has been found in the data.
    """
    # Split the response text into lines and extract hash-count pairs
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    # Check each hash in the response
    for h, count in hashes:
        if h == hash_to_check:
            return count  # Return the count if a match is found
    
    return 0  # Return 0 if the hash is not found

def pwned_api_check(password):
    """
    Checks if a password has been exposed in a data breach using the Pwned Passwords API.

    Args:
        password (str): The password to check.

    Returns:
        int: The number of times the password has been found in data breaches.
    """
    # Generate the SHA-1 hash of the password and convert it to uppercase
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    
    # Request data from the API using the first 5 characters of the hash
    response = request_api_data(first5_char)
    
    # Check the number of leaks using the remaining characters of the hash
    return get_password_leaks_count(response, tail)

def main(args):
    """
    Main function to check multiple passwords against the Pwned Passwords API.

    Args:
        args (list): A list of passwords to check.

    Returns:
        str: A message indicating that the process is done.
    """
    # Iterate over each password provided in the command line arguments
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    
    return 'done!'

if __name__ == '__main__':
    # Execute the main function with command line arguments, excluding the script name
    sys.exit(main(sys.argv[1:]))


# link to generate SHA1 Hash for password: https://passwordsgenerator.net/sha1-hash-generator/
# link to check password in pwned database: https://haveibeenpwned.com/Passwords
# link to check password in pwned database using API: https://haveibeenpwned.com/API/v3#PwnedPasswords    
# link to requests module: https://docs.python-requests.org/en/master/ 
# link to requests project: https://pypi.org/project/requests/

