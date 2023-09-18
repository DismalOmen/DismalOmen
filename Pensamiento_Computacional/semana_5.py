# 1 - CREAR DICCIONARIO PARA ESTUDIANTE, OTRO PARA VARIOS, LUEGO IMPRIMIR EL DE MAYOR EDAD.
# lista_estudiantes = [
#     {
#         'nombre': 'Juan Perez',
#         'DNI': '12345678A',
#         'edad': 17,
#         'curso': {
#             'año': 2023,
#             'division': 'A',
#             'orientacion': 'Ciencias'
#         }
#     },
#     {
#         'nombre': 'Maria Lopez',
#         'DNI': '98765432B',
#         'edad': 18,
#         'curso': {
#             'año': 2023,
#             'division': 'B',
#             'orientacion': 'Artes'
#         }
#     },
#     {
#         'nombre': 'Pedro Martinez',
#         'DNI': '56789012C',
#         'edad': 16,
#         'curso': {
#             'año': 2023,
#             'division': 'A',
#             'orientacion': 'Ciencias'
#         }
#     },
#     {
#         'nombre': 'Ana Ramirez',
#         'DNI': '34567890D',
#         'edad': 19,
#         'curso': {
#             'año': 2023,
#             'division': 'C',
#             'orientacion': 'Humanidades'
#         }
#     }
# ]

# # Inicializar variables para almacenar la edad mayor y el estudiante correspondiente
# edad_mayor = 0
# estudiante_mayor_edad = None

# # Iterar sobre la lista de estudiantes para encontrar al estudiante con la mayor edad
# for estudiante in lista_estudiantes:
#     if estudiante['edad'] > edad_mayor:
#         edad_mayor = estudiante['edad']
#         estudiante_mayor_edad = estudiante
# print(edad_mayor)

# necesitos del loop para poder revisar todos los datos del diccionario.
# edad_mayor crea una variable en 0 que luego es comparada con las demas edades para conseguir la mayor, mientras que estudiante_mayor_edad nos sirve para guardar todos los datos del mismo dentro de una variable.

# # 2 - CREAR LISTA DE PLANTAS, DONDE SE PUEDAN AGREGAR PLANTAS NUEVAS CON SUS ESPECIFICACIONES.

# def agregar_planta(lista_plantas, especie, necesita_luz_solar, precio):
#     # Crear un diccionario para representar la nueva planta
#     nueva_planta = {
#         'especie': especie,
#         'necesita_luz_solar': necesita_luz_solar,
#         'precio': precio
#     }

#     # Agregar la nueva planta a la lista de plantas
#     lista_plantas.append(nueva_planta)

# # Ejemplo de lista de diccionarios de plantas existente
# lista_plantas = [
#     {
#         'especie': 'Rosa',
#         'necesita_luz_solar': True,
#         'precio': 10.99
#     },
#     {
#         'especie': 'Lirio',
#         'necesita_luz_solar': False,
#         'precio': 8.99
#     }
# ]

# # Llamar a la función para agregar una nueva planta
# agregar_planta(lista_plantas, 'Orquídea', True, 12.99)

# # Imprimir la lista de plantas actualizada
# con printear el dic nos da toda la data dentro
# print(lista_plantas)
# si queremos datos especificos, podemos loopear y asociar los datos con la variable planta, la que nos va a permitir acceder
# a los demas datos para imprimirlos en orden por ejemplo.
# print("Lista de Plantas:")
# for planta in lista_plantas:
#     print("Especie:", planta['especie'])
#     print("Necesita Luz Solar:", planta['necesita_luz_solar'])
#     print("Precio:", planta['precio'])
#     print()

# 3 IMPRIMIR TICKET TOTAL PRECIOS.

# lista_productos = [
#     {
#         'producto': 'oreos',
#         'cantidad': 3,
#         'precio': 500
#     },
#     {
#         'producto': 'aceite de oliva',
#         'cantidad': 2,
#         'precio': 5000
#     },
#     {
#         'producto': 'Agua 6L',
#         'cantidad': 2,
#         'precio': 540
#     },
#     {
#         'producto': 'coca cola',
#         'cantidad': 1,
#         'precio': 500
#     }
# ]

# total_precio = 0

# for productos in lista_productos:
#     ticket = productos['cantidad'] * productos['precio']
#     print(productos['producto'])
#     print(ticket)

# 4 PELICULAS Q SUPEREN EL 7 PASAN

# lista_peliculas = [
#     {
#         'pelicula': '2001',
#         'año': 1968,
#         'puntaje': 6
#     },
#     {
#         'pelicula': 'batman begins',
#         'año': 2005,
#         'puntaje': 6
#     },
#     {
#         'pelicula': 'her',
#         'año': 2013,
#         'puntaje': 8
#     },
#     {
#         'pelicula': 'john constantine',
#         'año': 2005,
#         'puntaje': 7
#     }
# ]

# for pelis in lista_peliculas:
#     if pelis['puntaje'] >= 7:
#         print("-------------------------------")
#         print(f"""
# Nombre: {pelis['pelicula']}
# Año: {pelis['año']}
# Puntaje: {pelis['puntaje']}
#         """)
#         print("-------------------------------")
# 5 PROMEDIO NOTAS DE ALUMNO

# lista_nombres = [
#     {
#         'nombre': 'joaco',
#         'apellido': 'fuck v2',
#         'intento': 1,
#         'nota':4,
#     },
#     {
#         'nombre': 'joa',
#         'apellido': 'catch',
#         'intento': 1,
#         'nota':5,
#     },
#     {
#         'nombre': 'joaq',
#         'apellido': 'texting',
#         'intento': 1,
#         'nota':6,
#     },
#     {
#         'nombre': 'quin',
#         'apellido': 'idk',
#         'intento': 1,
#         'nota':7,
#     }
# ]

# cantidad_alumnos = len(lista_nombres)
# total = 0
# for estudiantes in lista_nombres:

#     total_notas = (estudiantes['nota'])

#     total += total_notas

#     promedio = total / cantidad_alumnos

# print(promedio)

# 6 LISTA DE PRODUCTO QUE PASEN CONTROL DE CALIDAD

# lista_productos = [
#     {
#         'codigo producto': 666,
#         'fecha de vencimiento': 666,
#         'control calidad': False,

#     },
#     {
#         'codigo producto': 777,
#         'fecha de vencimiento': 777,
#         'control calidad': True,

#     },
#     {
#         'codigo producto': 888,
#         'fecha de vencimiento': 888,
#         'control calidad': False,

#     },
#     {
#         'codigo producto': 999,
#         'fecha de vencimiento': 999,
#         'control calidad': True,

#     }
# ]
# defecto = []
# apto = []
# for productos in lista_productos:
#     if productos['control calidad'] == False:
#         defecto.append(productos['codigo producto'])
#     else:
#         apto.append(productos['codigo producto'])
# print(f"pasaron el control: {apto}")
# print(f"no pasaron el control: {defecto}")

# 7 LISTA MARATONES (FALTA MEJORAR)

# lista_nombres = [
#     {
#         'nombre': 'joaco',
#         'DNI': 'fuck v2',
#         'maratones totales': 'Maraton A, Maraton B, Maraton C',
#         'maratones': [
#             {'nombre': 'Maraton A',
#              'tiempo': '3:30'},
#             {'nombre': 'Maraton B',
#              'tiempo': '4:15'},
#             {'nombre': 'Maraton C',
#              'tiempo': '3:10'},
#         ]
#     },
#     {
#         'nombre': 'aco',
#         'DNI': 'fuck v2',
#         'maratones totales': 'Maraton A, Maraton B',
#         'maratones': [
#             {'nombre': 'Maraton A',
#              'tiempo': '3:30'},
#             {'nombre': 'Maraton B',
#              'tiempo': '4:15'},
#         ]
#     },
#     {
#         'nombre': 'quin',
#         'DNI': 'fuck v2',
#         'maratones totales': 'Maraton A',
#         'maratones': [
#             {'nombre': 'Maraton A', 'tiempo': '3:30'},
#         ]
#     }
# ]
# nombres = []
# tiempos = []
# for corredores in lista_nombres:
#     nombres.append(corredores['nombre'])
#     maratones = corredores['maratones']
#     for maraton in maratones:
#         tiempos.append(maraton['tiempo'])

# print(sorted(nombres), sorted(tiempos[0:3]),sorted(tiempos[3:5]), (tiempos[5]))