#Deep Thought
#Let's create an answer variable for the great question
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#create conditions for answers
if answer == "42":
    print("Yes")
elif answer.lower() == "forty-two":
    print("Yes")
elif answer.lower() == "forty two":
    print("Yes")
else:
    print("No")
