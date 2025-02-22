#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

def match_str(input_str):
    pattern = re.compile(r'a.*b$')
    if pattern.match(input_str):
        return True
    else:
        return False
inp_user = input("String: ")
if match_str(inp_user):
    print("Yes")
else:
    print("No")
