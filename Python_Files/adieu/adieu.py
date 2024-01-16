import inflect
p = inflect.engine()

my_list = []

while True:
    try:
        x = input("")
        # adds input to the empty list
        my_list.append(x)
        listed = p.join(my_list)


    except EOFError:
        print("Adieu, adieu, to", listed)
        break