# fty = 50

# print("Amount due ",fty)

# x = int(input("Intert Coin: "))

# result = fty - x
# total = 0
# results = result - x

# while result != 0:

#     print("Amount due:", result)
#     x = int(input("Instert Coin: "))


#     if results < result and results != 0:
#         print("Amount due:", results)
#         x = int(input("Instert Coin: "))


#     elif results == 0:

#             print("Changed owed:", results)
#             break



fty = 50

while fty > 0:

    print("Amount due:",fty)
    x = int(input("Insert Coin: "))

    if x in [25, 10, 5]:
        fty -= x

final = fty
print("Changed Owed:",final)








