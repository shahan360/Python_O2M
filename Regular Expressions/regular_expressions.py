# Import the regular expressions (re) module for pattern matching in strings
import re 

# Define a string containing various phrases
string = "this is a really cool tech from Dr. Doom's foundry that is going to optimize awesome stark tech with superior gypsy dark magical powers"

# Search for the word 'really' in the string
a = re.search('really', string)

# Print the Match object returned by re.search, which contains information about the match
print(a)

# The following four commands will raise an AttributeError if 'a' is None (i.e., if 'really' is not found).
# To avoid errors, ensure that 'really' exists in the string before calling these methods.
print(a.span())   # Print the start and end positions of the matched string
print(a.start())  # Print the starting position of the matched string
print(a.end())    # Print the ending position of the matched string
print(a.group())  # Print the actual matched string

# Compile the pattern 'really' for more efficient repeated searches
pattern = re.compile('really')

# Search for the first occurrence of 'really' in the string
b = pattern.search(string)

# Find all occurrences of 'really' in the string
c = pattern.findall(string)

# Compile a more complex pattern that matches the entire string
pattern = re.compile("this is a really cool tech from Dr. Doom's foundry that is going to optimize awesome stark tech with superior gypsy dark magical powers")

# Check if the entire string matches the pattern exactly
d = pattern.fullmatch("this is a really cool tech from Dr. Doom's foundry that is going to optimize awesome stark tech with superior gypsy dark magical powers")

# Attempt to match a different string to see if it exactly matches the pattern (should return None)
e = pattern.fullmatch("Hey Cap, this is a really cool tech from Dr. Doom's foundry that is going to optimize awesome stark tech with superior gypsy dark magical powers")  # This should return None, as it doesn't match exactly

# Compile the pattern 'really' again for different matching methods
pattern = re.compile('really')

# Attempt to match 'really' at the start of the string (this will succeed)
f = pattern.match('really cool tech')  # Starts matching from the beginning of the string

# Attempt to match 'really' from the start of a different string (this will return None)
g = pattern.match('yes really')  # Does not match as it does not start from the first character

# Print the results of the various matches and searches
print(f"b: {b}")  # Output of the search for 'really'
print(f"c: {c}")  # List of all occurrences of 'really'
print(f"d: {d}")  # Full match result for the first string
print(f"e: {e}")  # Full match result for the second string (should be None)
print(f"f: {f}")  # Match result for 'really cool tech'
print(f"g: {g}")  # Match result for 'yes really' (should be None)

'''
Additional Resources for Learning Regular Expressions (RegEx):

1. W3Schools Python RegEx Tutorial: 
   https://www.w3schools.com/python/python_regex.asp

2. RegexOne - Interactive Regex Tutorial: 
   https://regexone.com/

3. Regex101 - Online RegEx Tester and Debugger: 
   https://regex101.com/
'''
