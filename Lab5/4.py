#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

def sequence(input_str):
    pattern = re.compile(r'[A-Z][a-z]+')
    sequences = pattern.findall(input_str)
    return sequences

user_input = input("String: ")
sequences = sequence(user_input)
print("Sequences found:", sequences)
