import sys
from os.path import splitext
from PIL import Image, ImageOps
#<>
def checks():
    x = splitext(sys.argv[1])
    y = splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif x[1] == y[1]:
        pass
    else:
        sys.exit("Input and output have different extensions")

checks()
if len(sys.argv) == 3:
    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        right_size = shirt.size
        resized = ImageOps.fit(image, right_size)
        resized.paste(shirt, shirt)
        resized.save(sys.argv[2])
    except FileNotFoundError:
        raise FileNotFoundError