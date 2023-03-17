import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digits = re.findall("[0-9]", s)
    checks = len(s) <= 6 and len(s) >= 2 and s[-1].isdigit() and s[0].isalpha() and s[1].isalpha() and digits[0] != '0' and s.isalnum()
    if checks:
        if s[-2].isalpha():
            return s[-3].isalpha() and s[-4].isalpha()
        elif s[-3].isalpha():
            return s[-4].isalpha()
        else: 
            return True
    else:
        return False
         


main()
