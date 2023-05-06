import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)"', s)
    if match:
        url = match.group(1)
        return url.replace('youtube.com/embed/', 'youtu.be/')
    return None


if __name__ == "__main__":
    main()
