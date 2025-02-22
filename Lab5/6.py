#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

def replace(input_string):
    pattern = r'[ ,.]'
    replaced_str = re.sub(pattern, ':', input_string)
    return replaced_str
user_input = input("Enter a string: ")
res= replace(user_input)
print("New string:", res)
