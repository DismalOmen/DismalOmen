notas = [
    {"nombre": "Juan", "apellido": "Perez", "dni": "12345678", "nota": 7},
    {"nombre": "Ana", "apellido": "Gomez", "dni": "23456789", "nota": 5},
    {"nombre": "Pedro", "apellido": "Lopez", "dni": "34567890", "nota": 3},
    {"nombre": "Maria", "apellido": "Rodriguez", "dni": "45678901", "nota": 8},
]

nombre_archivo = "notas.csv" 

archivo = open("nombre_archivo","w")

archivo.write("nombre,apellido,dni,nota\n") 
archivo.write("\n")

for nota in notas:
    linea = f"{nota['nombre']},{nota['apellido']},{nota['dni']},{nota['nota']}\n"
    archivo.write(linea)
    archivo.write("\n")
    if nota['nota'] >= 4:
        print(f"el alumno {nota['nombre']} {nota['apellido']} aprobo con {nota['nota']}")


