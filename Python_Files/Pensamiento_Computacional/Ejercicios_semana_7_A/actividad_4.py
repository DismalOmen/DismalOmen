texto = "trabal.txt"
og = input("ingrese palabra a remplazar: ")
new = input("ingrese palabra nueva: ") 

archivo = open(texto, "r")
text = archivo.read()
archivo.close()

texto_remplazado = text.replace(og, new)

archivo = open(texto, "w")
text = archivo.write(texto_remplazado)
archivo.close()

