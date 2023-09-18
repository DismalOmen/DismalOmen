import tabulate
import sys

def sicilian():
    sicilian_table = [
            ["Cheese","$25.50","$39.95"],
            ["1 item","$27.50","$41.95"],
            ["2 items","$29.50","$43.95"],
            ["3 items","$31.50","$45.95"],
            ["Special","$33.50","$47.95"]]
    sicilian_head = ["Sicilian Pizza","Small","Large"]
    return(tabulate.tabulate(sicilian_table,headers = sicilian_head, tablefmt="grid"))

def regular():
    regular_table = [
            ["Cheese","$13.50","$18.95"],
            ["1 topping","$14.75","$20.95"],
            ["2 toppings","$15.95","$22.95"],
            ["3 toppings","$16.95","$24.95"],
            ["Special","$18.50","$26.95"]]
    regular_head = ["Regular Pizza","Small","Large"]
    return(tabulate.tabulate(regular_table,headers = regular_head, tablefmt="grid"))

def one_argument():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

def few_arguments():
    if len(sys.argv) < 1:
        sys.exit("Too few command-line arguments")

def wrong_syntax():
    values = ["regular.py","regular.csv","sicilian.py","sicilian.csv"]
    x = str(sys.argv[1])
    if x not in values:
        sys.exit("Not a python file")
    # if x.startswith("regular") or x.startswith("sicilian") and  x.endswith(".py") or x.endswith(".csv"):
    #     pass
    # else:
    #     sys.exit("Not a python file")

one_argument()
few_arguments()
wrong_syntax()


if sys.argv[1] == "regular.py" or sys.argv[1] == "regular.csv":
    print(regular())
elif sys.argv[1] == "sicilian.py" or sys.argv[1] == "sicilian.csv":
    print(sicilian())
