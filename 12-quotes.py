#Exercise: Quotes

#ask users authors and creates fiction characters quotes
author = input("Author: ")
qoutes = {"Obi-Wan Kenobi": "These aren't the droids you're looking for.",
          "Sirius Black": "If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals.",
          "Darth Vader": "NO … I AM YOUR FATHER…",
          "Forrest Gump": "Life is like a box of chocolates. You never know what you're gonna get.",
          "Hamlet": "To be, or not to be"}
print(f"{author} says, \"{qoutes[author]}\"")
