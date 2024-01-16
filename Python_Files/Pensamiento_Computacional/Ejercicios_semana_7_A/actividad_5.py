def mostrar_producto(producto):
    print(f"Nombre producto: {producto['nombre']}")
    print(f"Código producto: {producto['código']}")
    print(f"Precio por unidad: {producto['precio']}")
    print(f"Stock: {producto['stock']}")

def agregar_producto(diccionario):
    producto = "dict.txt"
    archivo = open(producto,"a")
    formato = f"{diccionario['nombre']};{diccionario['código']};{diccionario['precio']};{diccionario['stock']}\n"
    archivo.write(formato)
    archivo.write("\n")
    archivo.close()

producto_nuevo = {
    "nombre": "hojas A4",
    "código": 35662,
    "precio": 600,
    "stock": 45
}

mostrar_producto(producto_nuevo)

agregar_producto(producto_nuevo)