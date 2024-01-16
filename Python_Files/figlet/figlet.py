import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

#Specific font
if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] == figlet.getFonts():
    x = input("Input: ")
    figlet.setFont(font= sys.argv[2])
    print("Output:",figlet.renderText(x))

#Exit
elif sys.argv[1] != "-f" or sys.argv[1] != "--font" and sys.argv[2] != figlet.getFonts():
    sys.exit("Invalid Usage")

#Random font
elif len(sys.argv) == 1:
    rng = random.choice(figlet.getFonts())
    y = input("Input: ")
    print("Output:", figlet.renderText(rng))




