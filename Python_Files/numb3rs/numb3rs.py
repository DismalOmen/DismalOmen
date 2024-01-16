import re
import sys
#<> ^ \

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("True")
    else:
        print("False")

def validate(ip):
    correct = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip)
    if correct:
        return True
    else:
        return False



...


if __name__ == "__main__":
    main()