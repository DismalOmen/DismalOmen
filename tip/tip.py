def main():
    dollars = dollars_to_float(input("How much was the meal? "))

    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip =  ((dollars * percent) /100)


    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):

       dollars_to_float = float(dollars.lstrip("$"))

       return(dollars_to_float)

def percent_to_float(percent):

       percent_to_float = float(percent.replace("%", " "))

       return(percent_to_float)

main()