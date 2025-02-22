#Write a Python program to insert spaces between words starting with capital letters.

def insert_spaces(input_str):
    new_string = ""
    for i, char in enumerate(input_str):
        if char.isupper() and i != 0:
            new_string_string += " "
        new_string += char
    
    return new_string

input_str = input("String: ")

res = insert_spaces(input_str)

print("New string:", res)
