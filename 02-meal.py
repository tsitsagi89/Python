#Exercise "Meal Time"

def main():
    t = input("What time is it? ")
    if convert(t) >= 7.0 and convert(t) <= 8.0:
        print("breakfast time")
    elif convert(t) >= 12.0 and convert(t) <= 13.0:
        print("lunch time")
    elif convert(t) >= 18.0 and convert(t) <= 19.0:
        print("lunch time")


def convert(time):
    time = float(time.split(":")[0]) + float(time.split(":")[-1])/60
    return time


if __name__ == "__main__":
    main()
