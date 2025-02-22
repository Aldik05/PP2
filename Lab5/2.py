#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

input_str = input("String: ")

pattern = re.compile(r'a(bb{1,2})')

if pattern.search(input_str):
    print("Yes")
else:
    print("No")
