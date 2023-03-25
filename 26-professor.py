import random

def main():
    level = get_level()
    score = test(level)
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        levels = ["1", "2", "3"]
        if level not in levels:
            continue
        else:
            return level


def generate_integer(level):
    if level == "1":
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return x, y
    elif level == "2":
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y
def tries(x, y):
    try_number = 1
    while try_number <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True
            else:
                try_number += 1
                print("EEE")
        except ValueError:
            try_number += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

def test(level):
    test_number = 1
    score = 0
    while test_number <= 10:
        x, y = generate_integer(level)
        check_test = tries(x, y)
        if check_test == True:
            score += 1
        test_number += 1
    return score

if __name__ == "__main__":
    main()
