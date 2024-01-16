months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
]

while True:
    try:



        x = input("Date: ")

        if x.__contains__("/"):
            m,d,y = x.split("/")

        elif x.__contains__(","):
            md,y = x.split(",")
            m,d = md.split(" ")




        if m not in months:
            pass
        elif m.isalpha():
            m = int(months[0:11].index(m)) + 1
            if m <= 9:
                m = "0" + str(m)
            if int(d) <= 9:
                d = "0" + str(d)

            print(f"{y}-{str(m)}-{d}")
            break
        elif int(m) <= 9 and int(d) <= 9:
            print(f"{y}-0{m}-0{d}")
            break
        elif int(d) <= 9 and int(m) > 9:
            print(f"{y}-{m}-0{d}")
            break
        else:
            print(f"{y}-{m}-{d}")
            break

    except:
        pass



