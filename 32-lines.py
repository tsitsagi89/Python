import sys

try:
    with open(f"{sys.argv[1]}", "r") as file:
        count_lines = 0
        for line in file:
            if line != "\n" and not line.startswith("#"):
                count_lines += 1
except FileNotFoundError:
    sys.exit("File Not Found")

print(count_lines)
