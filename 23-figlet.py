import sys
import random
from pyfiglet import Figlet
figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
    figlet.setFont(font=f)
    text = input("Input: ")
    print("Output:", "\n", figlet.renderText(text))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet.setFont(font=sys.argv[2])
    text = input("Input: ")
    print("Output:", "\n", figlet.renderText(text))
else:
    print("Invalid usage")
    sys.exit(1)
