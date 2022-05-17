#manejo de excepciones con python
import os

#respuesta = int(input("Ingresa un número: "))

os.system('cls')

try:
    respuesta = int(input("Ingresa un número: "))
except Exception as ex:
    print(f"Hubo una excepción => {ex}")

print("Se manejo bien la excepción")

#ejemplo de excepcion de documentacion
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")