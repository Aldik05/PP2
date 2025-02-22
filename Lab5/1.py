#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
#for any txt file :

import re

a = input("String: ")
pattern = r'ab*'
match = re.search(pattern, a)

if match:
    print(f"'{pattern}' yes")
else:
    print(f"'{pattern}' no")

