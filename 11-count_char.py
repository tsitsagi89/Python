#Exercise: "counting of characters"

text = input("Write any text ")
count_char = len(text)
if count_char > 0:
    print(f"{text} has {count_char} characters.")
else:
    print("Text input is mandatory")
