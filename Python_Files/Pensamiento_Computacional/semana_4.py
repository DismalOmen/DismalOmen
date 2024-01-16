# 1 y 2
# list = [1,2,3,4,5,6,7,8,9,10]
# print(list[4])
# print(len(list))

# -------------------------------
# 3 y 4
# list = [244, 255, 674, 673, 924, 2344]
# list.sort()
# print(list[0],list[5])

# -------------------------------
# 5
# tuple = ('joaco', 24)
# print(tuple[1])

# -------------------------------
# 6
# list1 = ["joaco", "presagio", "omen", "joaquin", "jua"]

# ultimo_elemento = len(list1) - 1
# anteultimo_elemento = len(list1) - 2

# list1[ultimo_elemento] = "Juan"

# print(list1, list1[anteultimo_elemento], list1 * 3)

# --------------------------------
#7

# tuple = ('joaco', 24)
# tuple0 =('jua',23)
# tuple1 =('joaquin', 00)
# list = []
# list.append(tuple)
# list.append(tuple0)
# list.append(tuple1)
# print(list)

# -------------------------------
#8 imprimir continente pais y capital
# paises = [
#     ("Francia", "París", "Europa"),
#     ("Argentina", "Buenos Aires", "América del Sur"),
#     ("Japón", "Tokio", "Asia"),
#     ("Alemania", "Berlín", "Europa"),
#     ("Perú", "Lima", "América del Sur"),
# ]

# def imprimir_paises(paises):
#     for pais in paises:
#         print(f"País: {pais[0]} \nCapital: {pais[1]} \nContinente: {pais[2]} \n")

# imprimir_paises(paises)

# ---------------------------------
#9 libros repetidos en lista
# libros = ["el aleph", "El castillo de Ontrato", "El diccionaro del diablo", "Cancion de fuego y hielo", "Meditaciones Metafisicas", "El diccionaro del diablo", "Cancion de fuego y hielo"]
# ejemplares = {}

# for libro in libros:
#     if libro not in ejemplares:
#         ejemplares[libro] = 1
#     else:
#         ejemplares[libro] += 1

# print(f"{ejemplares}")

# ------------------------------------
# 10
# list = [1,2,3,4,5,6,7,8,9,10]

# for listed in list:
#     list0 = []
#     list0.append(listed ** 2)
#     print(list0)

# ------------------------------------

# 11 unir frase
# list = ["entender","pueden","humanos", "los", "que", "codigo","escriben","programadores","buenos","lo","entiende","computadora","una","que","codigo","escribe","tonto","cualquier"]
# list.reverse()
# frase = ""
# for _ in list:
#     frase += ' ' + _
# print(frase)

#------------------------------------
#12
# materias = ""
# while True:
#     x = input("agregue la materia que quiera: ")
#     if x not in materias and x != 'x':
#         materias += '-' + x + '-'
#     if x == 'x':
#         print(materias)
#         break
# -------------------------------------
# 13 TICKES DE SUPER
# list = [("Lavandina", 300), ("coca-cola",500)]
# list0 = [("Super Lavandina", 600), ("coca-cola super",700)]
# total = 0
# for value in list:
#     total += value[1]
# for value0 in list0:
#     total += value0[1]
# print(f"${total}")

# --------------------------------------
# SEGUNDA PARTE
# 1
# list = ['a','e','i','o','u']
# string = "well, see you later innovator"
# for _ in string:
#     if _ in list:
#         print(_, end = " ")

# --------------------------------------
# 2 dar vuelta un string

# string = "live again, all roads end, i'll be coming home"
# list = []
# frase = ""
# for _ in string:
#     list.append(_)
# list.reverse()
# for _ in list:
#      frase += '' + _
# print(frase)

# --------------------------------------
# 3 eliminar el substring
# string = "open c-74, smalls"
# s = string[10::]
# print(string[:9])

# --------------------------------------
# 4 agregar un ingrediente a la lsita
# list = ["tomate","queso","cebolla","albahaca"]

# while True:
#     try:
#         x = input("agregue un ingrediente: ")
#         if x not in list:
#             list.append(x)
#             print(list)
#             break
#     except:
#         pass

# ------------------------------------
# 5 agregar "carta" en creciente

# list = [1,2,4,7]
# nueva_carta = 5
# list.append(nueva_carta)
# list.sort()
# print(list)

# -----------------------------------
#