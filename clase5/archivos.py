#practica de manipulación de open

archivo = open("texto.txt", "w")

archivo.write("Hola Mundo")

#Cierra el archivo que se esta manipulando
archivo.close()

print("Terminó la manipulación de archivos")