def main():
    greeting = input("Greeting: ")
    value_of_greeting = value(greeting)
    print(f"${value_of_greeting}")
    
def value(greeting):

    word = "Hello"
    word0 = "Hello Newman"

    if word in greeting:
        return (0)

    elif word0 in greeting:
        return (0)

    elif greeting.startswith("H"):
        return (20)

    else:
        return (100)


if __name__ == "__main__":
    main()








