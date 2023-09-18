menu = {
}

total = 0
while True:

    try:
        x = input("")
        if x in menu:
            menu[x] += 1
        else:
            menu[x] = 1


    except (EOFError):

        for key in sorted(menu.keys()):
            print(menu[key], key.upper())

        break


    except (KeyError):
        pass


