#converting text into emoji

#lets create main function, that prompts the user for input texts and call convert function
def main():
    n = str(input("Write a smile "))
    return print(convert(n))
# create function, that convert text into emoji
def convert(x):
    if x == ":)":
        return "🙂"
    elif x == ":(":
        return "🙁"
    else:
        return x

main()
