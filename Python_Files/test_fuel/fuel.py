def main():
    fraction = input("Fraction: ")
    convertion = convert(fraction)
    printed = gauge(convertion)
    print(printed)

def convert(fraction):
    while True:
        try:
            x, y= fraction.split("/")
            x_inted = int(x)
            y_inted = int(y)
            if x_inted >= 1 and y_inted >= 1 and x_inted <= y_inted or x == "0" and y == "100":
                p = ((x_inted / y_inted) * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")
            raise

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage:,.0f}%")



if __name__ == "__main__":
    main()
