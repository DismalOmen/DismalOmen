import sys
#><
def one_argument():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def few_arguments():
    if len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")

def wrong_syntax():
    x = str(sys.argv[1])
    if x.endswith(".py"):
        pass
    else:
        sys.exit("Not a python file")

count = 0
one_argument()
few_arguments()
wrong_syntax()

with open(sys.argv[1]) as file:
    try:
        for line in file:
            count += 1
            if line.isspace():
                count -= 1
            elif line.strip().startswith("#"):
                count -= 1
        print(count)
    except:
        raise FileNotFoundError