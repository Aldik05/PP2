#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

def sequence(input_str):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    sequences = pattern.findall(input_str)
    return sequences
user_inp = input("Enter a string: ")
seq = sequence(user_inp)
print("Sequences found:", seq)
