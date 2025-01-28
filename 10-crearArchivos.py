from io import open
import math

text=open("archivo.txt","w")
text.write("Hola, soy un archivo de texto \n")
text.write("Hola, Mundo \n")



lectura=""
texto=open("archivo.txt","r")
lectura=texto.readlines()
print(type(lectura))
print(lectura)
for i in lectura:
    print(i)
texto.close()