#Write a python program to convert snake case string to camel case string.

def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = ''.join(word.capitalize() for word in words)
    return camel_case

snake_case_s = input("Snake case string: ")

camel_case_s = snake_to_camel(snake_case_s)

print("Camel case string:", camel_case_s)
