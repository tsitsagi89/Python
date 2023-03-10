#Exercise: Home Federal Savings Bank
#Create greeting ignored any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
greeting = input("Greeting: ").strip().lower()

#conditionals by greetings
if greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
