archivo = open("regalo.txt","r")
count = 0
monto = 1000

for _ in archivo:
    count += 1
print(count * monto) 
archivo.close()

archivo = open("regalo.txt","r")
nombres = archivo.read()
archivo.close()

if "santi" in nombres:
    nombres_lista = nombres.split()
    nombres_lista.append("tomy")
    nombres_act = ' '.join(nombres_lista)
    archivo = open("regalo.txt","w")
    archivo.write(nombres_act)
    archivo.close()
else:
    print("santi no esta!")

print(nombres_act)

