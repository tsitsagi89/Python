import inflect
p = inflect.engine()
names = []
try:
    while True:
        name = input("Name: ")
        names.append(name)

except EOFError:
    print("Adieu, adieu, to", p.join(names, final_sep=""))
