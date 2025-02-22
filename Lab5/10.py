#Write a Python program to convert a given camel case string to snake case.

def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case
camel_case_str = input("Camel case string: ")

snake_case_str = camel_to_snake(camel_case_str)

print("Snake case string:", snake_case_str)
