# loop user input until number is in range(1,8)
while True:
    try:
        height = int(input("Height: "))
        # break when correct range
        if height >= 1 and height <= 8:
            break
    except:
        pass
# 3 loops, one for making each row, one for making the image backwards, and one for hashes
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(i):
        print("#", end="")
    # print here so we get a new line
    print()