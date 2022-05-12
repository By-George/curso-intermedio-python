import os

#funcion para crear carpetas
def crear_carpetas(sufijo, cantidad):
    for i in range(cantidad):
        os.mkdir(f"{sufijo}{i+1}")
        print(f"Creando carpeta: {sufijo}{i+1}")

def borrar_carpetas(sufijo, cantidad):
    for i in range(cantidad):
        os.rmdir(f"{sufijo}{i+1}")
        print(f"Borrando carpeta: {sufijo}{i+1}")