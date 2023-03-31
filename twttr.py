
def main():
    tweet = input("input text: ")
    print(shorten(tweet))


def shorten(x):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for i in vowels:
        x = x.replace(i, '').lower()
    return x
   

if __name__ == "__main__":
    main()