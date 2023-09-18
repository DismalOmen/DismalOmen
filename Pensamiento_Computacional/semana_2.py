def main():
    uno()
    dos()
    tres()
    cuatro()
    cinco()
    seis()
    siete()
    nueve()
    diez()
    once()
    doce()

def uno():
    entero = input("Ingrese un número entero: ")
    print("el numero ingresado corresponde a", entero)

def dos():

    x = int(input("Ingrese un entero: "))
    y = int(input("Ingrese un entero: "))

    suma = x + y
    resta = x - y
    multi = x * y
    divisionE = x / y
    divisionR = x % y

    print("Suma:",suma, "Resta:", resta,"Multiplicacion:", multi, "Division Entera:",divisionE, "Division Resto:",divisionR)

def tres():
    x = int(input("Ingrese un entero: "))

    if x % 2 == 0:
        print("El número es par!")
    else:
        print("Número impar!")

def cuatro():
    x = int(input("Ingrese su año de nacimiento: "))
    y = int(input("Ingrese cualquier año posterior para saber su edad en el mismo: "))

    calculo = y -x

    print(f"Su edad seria {calculo} años.")

def cinco():
    x = int(input("Ingrese un entero: "))
    y = int(input("Ingrese un entero: "))
    z = int(input("Ingrese un entero: "))
    w = int(input("Ingrese un entero: "))
    n = int(input("Ingrese un entero: "))

    calculo = (x + y + z + w + n) / 5

    print(f"El promedio de los numeros ingresados es: {calculo}")

def seis():
    x = int(input("Ingrese un número: "))

    calculo = x - 1, x + 1

    print(calculo)

def siete():
    x = str(input("Ingrese un string: "))
    y = input("Ingrese un entero: ")

    print(f"{x + y}")

def ocho(numero, numero0):
    return numero / numero0, numero % numero0

def nueve():
    x = str(input("Ingrese su nombre: "))
    y = str(input("Ingrese su apellido: "))

    print(f"{y}, {x}")

def diez():
    counter = 0
    x = input("Ingrese una palabra: ")
    for _ in x:
        counter += 1

    print(f"La cantidad de letras correspode a: {counter} ")

def once():
    x = input("Ingrese una palabra: ")
    print(x[0:5])

def doce():
    x = input("Ingrese una palabra: ")
    x0 = x.replace('a', '')
    print(x0)





if __name__ == "__main__":
    main()
