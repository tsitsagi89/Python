while True:
    try:
        fraction = float(eval(input("Fraction: ")))
        if fraction > 1:
            continue
        elif fraction <= 0.01:
            print("E")
            break
        elif 0.99 <= fraction <= 1:
            print("F")
            break
        else:
            print("{:.0%}".format(fraction))
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except NameError:
        pass

    
