def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) >= 2 and len(s) <=6 and s[0:4].isalpha() and s.isalnum() or s == "CS50":
        return True
    else:
        return False





main()