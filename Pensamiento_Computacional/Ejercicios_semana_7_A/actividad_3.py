archivo_compras = open("compras.txt","w")

lista_compras = []

while True:
    producto = input("ingrese producto:")
    print("salir con X")

    if producto.upper() == 'X':
        break
    lista_compras.append(producto)

for producto in lista_compras:
    archivo_compras.write(producto + '\n')

archivo_compras.close()