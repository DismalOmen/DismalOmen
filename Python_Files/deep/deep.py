x = input("What is the Answer to the Great Quesstion of Life, the Universe, and Everything?: ").strip()
match x:
    case "42" | "forty-two" | "forty two" | "FoRty TwO":
        print("Yes")
    case _:
        print("No")
