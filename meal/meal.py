def main():

    time = convert(input("What time is it? "))

    if time >= 7 and time <= 8:
        print("breakfast time")

    elif time >= 12 and time <= 13:
        print("lunch time")

    elif time >= 18 and time <= 19:
        print("dinner time")

    else:
     print()


def convert(time):

    (h, m) = time.split(':')

    time = (int(h) * 60 + int(m)) / 60

    convert = float(time)

    return(convert)


if __name__ == "__main__":
    main()