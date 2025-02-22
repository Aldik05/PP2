#Write a Python program to split a string at uppercase letters.

def split_at_uppercase(input_str):
    parts = []
    start = 0
    for i, char in enumerate(input_str):
        if char.isupper():
            parts.append(input_str[start:i])
            start = i
    parts.append(input_str[start:])
    
    return parts

input_str = input("String: ")

result = split_at_uppercase(input_str)

print("Parts of the string:", result)
