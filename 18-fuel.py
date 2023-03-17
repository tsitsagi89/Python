while True:
    try:
        fraction = float(eval(input("Fraction: ")))
        percentage = "{:.0%}".format(fraction)
        if fraction > 1:
            continue
        elif fraction <= 0.01:
            print("E")
            break
        elif 0.99 <= fraction <= 1:
            print("F")
            break
        else:
            print(percentage)
            break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    except NameError:
        continue

