def main():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    # averege of letters
    L = float((letters * 100) / words)
    # averege of sentences
    S = float((sentences * 100) / words)
    # math to get the grade level
    index = int(round(0.0588 * L - 0.296 * S - 15.8))
    # according index value is what we print under 0 before grade 1, in range 0 16 or 16+
    if index <= 0:
        print("Before Grade 1")
    elif index > 0 and index < 16:
        print(f"Grade {index}")
    else:
        print("Grade 16+")

# we get rid of spaces with replace, create a counter, simple for loop to count every character


def count_letters(text):
    txt = text.replace(" ", "")
    counter = 0
    for _ in txt:
        if _ != '.' and _ != '!' and _ != '?' and _ != ',':
            counter += 1
    return counter

# so we use split to literally split the text and then get his lenght once we do that just return value


def count_words(text):
    txt = len(text.split())
    return txt


def count_sentences(text):
    sentences = 0
    for _ in text:
        if _ == '!' or _ == '?' or _ == '.':
            sentences += 1
    return sentences


if __name__ == "__main__":
    main()
