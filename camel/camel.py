camel_case = input("camelCase:")
snake_case = ""

for c in camel_case:
    if c.isupper():
        snake_case += f'_{c.lower()}'
    else:
        snake_case += c

print("snakeCase:",snake_case)



