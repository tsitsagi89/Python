variable_name = input("camelCase: ")
for c in variable_name.strip():
    if c.isupper():
        c = "_" + c
    else:
        c
    print(c.lower(), end = '')
