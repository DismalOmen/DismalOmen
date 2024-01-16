salas_file = open('salas.txt', 'r')
salas_lines = salas_file.readlines()

peliculas_file = open('peliculas.txt', 'r')
peliculas_lines = peliculas_file.readlines()


funciones_csv = open('funciones.csv', 'w')
for i in range(len(salas_lines)):
    sala = salas_lines[i].strip()  
    pelicula = peliculas_lines[i].strip()  
    funciones_csv.write(f'{sala};{pelicula}\n')

funciones_csv.close()  
salas_file.close()
peliculas_file.close() 