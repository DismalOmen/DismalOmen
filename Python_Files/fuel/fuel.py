while True:
    try:
        x, y=(input("Fraction: ")).split("/")
        result = int(x) / int(y)
        final = int(result * 100)
        if final <= 1:
            print("E")
            break
        elif final >= 99:
            print("F")
            break
        else:
            print(f"{final}%")
            break

    except (ValueError, ZeroDivisionError):
        pass


