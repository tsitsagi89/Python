import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        elif level > 0:
            n = random.choice(range(1, level))
            while True:
                guess = int(input("Guess: "))
                if guess < 1:
                    continue
                else:
                    if guess > n:
                        print("Too large!")
                    elif guess < n:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break         
        else:
            continue
        break 
    except (ValueError, NameError):
        pass
    

