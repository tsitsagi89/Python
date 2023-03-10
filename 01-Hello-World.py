#Exercise 1. Version 1.

#make a variable and Ask users about their name
name = input("What is your name? ").strip()
#Concatenate text and variable
greeting = ("Hello, " + name.title() + ", nice to meet you!")
print(greeting)


#Exercise 1. Version 2.
print("Hello, " + input("what is your name? ").strip().title() + "," + " nice to meet you!")


#Exercise 1. Version 3.

#make a variable and Ask users about their name.

name = input("What is your name? ").strip()

#make conditionals, which responds to people with different names with different greetings.
if name == "Goga":
    print("Hello, " + name.title() + ", nice to meet you!")
elif name == "ოთო":
    print("გამარჯობა, " + name.title() + ", სასიამოვნოა თქვენი გაცნობა!")
elif name == "Giorgi":
    print("Hi, " + name.title() + ", nice to meet you!")
else:
    print("Hey, " + name.title() + ", nice to meet you!")
