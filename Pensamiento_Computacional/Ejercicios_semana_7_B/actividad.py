#                               1  y 2
# while True:
#     try:
#         pedilo = int(input("ingrese un numero entero: "))
#         pedilo0 = int(input("ingrese un numero entero: "))

#         print(f"su numero es {pedilo * pedilo0}")
#         break
#     except ValueError:
#         print("numero ingreso invalido")
# ---------------------------------------------------------------------
#                                3
# while True:
#     try:
#         divisor = float(input("Ingrese el divisor: "))
#         dividendo = float(input("Ingrese el dividendo: "))
        
#         if divisor == 0:
#             print("El divisor no puede ser 0. Intente de nuevo.")
#         else:
#             cociente = dividendo / divisor
#             print(f"El cociente es: {cociente}")
#             break 
#     except ValueError:
#         print("Por favor, ingrese valores numéricos válidos.")
#-----------------------------------------------------------------------
#                                4
# try:
#     file = open("file.txt","r")
#     archivo = file.read()

#     print("contenido: ")
#     print(archivo)
# except FileNotFoundError:
#     print("No existe el archivo")
#------------------------------------------------------------------------
#                                5
# def cinco(list, index):
#     try:
#         value = list[index]
#         if 0 <= index < len(list):
#             print(f"el valor en {index} es {value}")
#         else:
#             print("fuera de rango")
#     except IndexError:
#         print("error de lista")

# list0 = [23,454,64,444,666]
# index = 4

# cinco(list0,index)
#------------------------------------------------------------------------------
#                                6
# while True:
#     try:
#         print("numero de jugadores posibles: 2,3,4")
#         print()
#         valor = int(input("ingrese un numero de jugadores: "))
#         if valor < 2:
#             print("minimo 2 jugadores")
#         elif valor > 4:
#             print("maximo 4")
#         elif valor == 2 or valor == 3 or valor == 4:
#             print(valor)
#             break
#     except ValueError:
#         print("ingrese numero correcto")
#---------------------------------------------------------------------------------
#                                7
# while True:
#     try:
#         print("numero de jugadores posibles: 2,4,6")
#         print()
#         valor = int(input("ingrese un numero de jugadores: "))
#         if valor % 2 != 0:
#             print("deben ser pares")
#         elif valor < 2:
#             print("minimo 2 jugadores")
#         elif valor > 6:
#             print("maximo 6")
#         elif valor % 2 != 0:
#             print("deben ser pares")
#         elif valor == 2 or valor == 4 or valor == 6:
#             print(valor)
#             break
#     except ValueError:
#         print("ingrese numero correcto")
#--------------------------------------------------------------
#                           8
opciones = {
1: "hamburguesas",
2: "milanesas",
3: "gaseosa",
4: "alfajor",
5: "papas fritas",
6: "agua"
}

valores = {
1:1000,
2:1500,
3:500,
4:300,
5:600,
6:350
}


for op in opciones:
    producto = opciones[op]

    #si esa key esta en valores puedo pasar a una variable la info
    if op in valores:
        precio = valores[op]
        print(f"{op}: {producto}->{precio}")

while True:
    try:
        opcion = int(input("ingrese el numero de la opcion que desea: "))
        cantidad = int(input("ingrese la cantidad que desea: "))

        if opcion in opciones and cantidad > 0:
            precio_unidad = valores[opcion]
            total = precio_unidad * cantidad
            print(f"Total: {total}")
            break
        else:
            print("Ingrese una opcion valida")
            
    except ValueError:
        print("Entrada invalida.")

