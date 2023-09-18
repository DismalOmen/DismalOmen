# CUAL N ES MAYOR
# def func(value0, value1):
#     if value0 < value1:
#         return(f"{value0} es menor")
#     else:
#         return(f"{value0} es mayor")

# func(234,1)
# ------------------------------
# REVISAR SI ES VOCAL
# list = ['a','e','i','o','u']
# def vocal(n):
#     if n not in list:
#         print(f"{n} no es vocal")
#     else:
#         print(f"{n} es vocal")
# vocal('z')

# --------------------------------
# REVISAR SI ES NUMERO PAR Y MENOR A 10
# def pair_odd(n):
#     return n % 2 == 0 and n < 10
# if pair_odd(33):
#     print("cumple con los requisitos")
# else:
#     print("no cumple")
# -------------------------------
# DEVOLVER EL ABS DE UN NUMERO
# x = int(input("ingrese un numero: "))
# if x < 0:
#     print(x * -1)
# else:
#     print(x * 1)
# --------------------------------
# PIEDRA PAPEL O TIJERA IMPOSIBLE
# list = ['R', 'P', 'T']
# x = input("Juguemos! Ingresá piedra ( R), papel (P) o tijera (T): ").upper()
# while x in list:
#     if x == 'R':
#         print("papel, gane.")
#     elif x == 'P':
#         print("tijera, gane.")
#     else:
#         print("piedra, gane")
#     break
# else:
#     print("not in list")
# ------------------------------------
# 6     SUMA MENOR A 100 ETC
# def hundred(value, value0):
#     sum = value + value0
#     if sum < 100:
#         amount = 100 - sum
#         print(f"{amount} para llegar a 100")
#     else:
#         print("llega a 100")
# hundred(50,50)
# para que el programa no quede generalizado a 100,
# crearia una variable que lo remplace, tomando un input del usuario para tener el limite que quieraa
# ------------------------------------
# 7 ESTACIONES
# list = ['V','O','I','P']
# x = input("Ingrese la inicial de la estacion que desee: ").upper()
# if x in list:
#     if x == 'V':
#         print("Verano")
#     elif x == 'O':
#         print("Otoño")
#     elif x == 'I':
#         print("Invierno")
#     elif x == 'P':
#         print("Primeravera")
# else:
#     print("Ingrese la inicial de una estacion")
# --------------------------------------------------
# 8 CONTAR NUMEROS
# x = int(input("ingrese un numero: "))
# for _ in range(1, x + 1):
#     print(_)
# ----------------------------------------------------
# 9 MISMO PERO CON TABLAS DE *
# x = int(input("ingrese un numero: "))
# for _ in range(1, 11):
#      print(_ * x)

# --------------------------------------------------
# 10 FC X CANTIDAD DE VECES
# x = int(input("ingrese un numero: "))
# for _ in range(1, x + 1):
#     print("feliz cumpleaños")
# ----------------------------------------------------
# 11 COBRO AUTOMATICO
# entra un numero, usuario decide cuanto pagar hasta q sea 0 o menor
# def cobro(value):
#     while True:
#         try:
#             x = int(input("ingrese monto para pagar: "))
#             value -= x
#             print(f"restan {value} pesos")
#             if value <= 0:
#                 break
#         except:
#             pass
# cobro(10000)
# ---------------------------------------------------------
# 12 1-20 determinando cual es odd/pair

# for _ in range(1, 21):
#     if _ % 2 == 0:
#         print(f"{_} es par")
#     else:
#         print(f"{_} es impar")

# ------------------------------------------------------------
# 13 maquina q acepta x fichas
# def arcade(value):
#     counter = 0

#     while counter < value:
#         try:
#             sum = value - counter
#             x = input(f"ingrese {sum} fichas: ").upper()
#             if x == 'F':
#                 counter += 1
#             else:
#                 print("Ingrese una ficha ('F' o 'f')")
#         except:
#             pass
#     if counter == value:
#         print("A jugar!")

# arcade(3)
# -------------------------------------------------------------
# NUMEROS PRIMOS.
# def imprimir_primos(n):
#   for i in range(2, n + 1):
#     if i > 1:
#       for j in range(2, i):
#         if i % j == 0:
#           break
#       else:
#         print(i)
# imprimir_primos(25)