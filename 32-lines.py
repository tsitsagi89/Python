import sys

with open(f"{sys.argv[1]}", "r") as file:
    count_lines = 0
    for line in file:
        if line != "\n" and not line.startswith("#"):
            count_lines += 1
print(count_lines)
