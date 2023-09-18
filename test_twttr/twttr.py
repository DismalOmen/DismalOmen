def main():
    word = input("Input: ")
    print("Output: ", shorten(word))

def shorten(word):

    if word == word.upper():
        convert_ = word.replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
        return (convert_)
    else:
        convert = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").capitalize()
        return (convert)



if __name__ == "__main__":
    main()





