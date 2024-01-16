import random

while True:
    try:
        level = int(input("Level: "))
        n = random.randint(1,level)
        guess = int(input("Guess: "))

        if guess == n:
            print("Just Right!")
            break
        elif guess < n:
            print("Too small!")
        elif guess > n:
            print("Too large!")
    except ValueError:
        pass