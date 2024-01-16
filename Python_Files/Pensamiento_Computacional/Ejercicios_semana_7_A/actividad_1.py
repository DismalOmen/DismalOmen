archivo = open("texto.txt","r") 
leido = archivo.read()
print(leido)
archivo.close()

respuesta = input("rta: ") 

archivo = open("texto.txt","w")
escrito = archivo.write(leido + '\n' + respuesta + '\n')
archivo.close()

