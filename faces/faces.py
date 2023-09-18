def main():

    #Ask for input
    frase = input(" ")
    #Print result
    convert(frase)



def convert(frase):

    #Convert
    convert = frase.replace(":)", "🙂").replace(":(", "🙁")
    print(convert)


main()

