tweet = input("input text: ")
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in vowels:
    tweet = tweet.replace(i, '')

print(tweet)
