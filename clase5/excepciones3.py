import os
# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con Windows

# al crear un directorio si ya existe agregarle entre parentesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)
os.system('cls')

#contenido = os.listdir('D:\\Programacion\\Python\\Sistemas\\curso-intermedio-python')
#print(contenido)

def crear_directorio(carpeta):
    try:
        os.mkdir(carpeta)
        print(f"Se creó la carpeta {carpeta}")
    except FileExistsError as FEerror:
        return False
    except FileNotFoundError as ex:
        print("No se encontro el directorio proporcionado")
    except Exception as ex:
        print("oops ocurrio un error")

i = 1

if crear_directorio("carpeta_nueva") is False:
    while crear_directorio(f"carpeta_nueva({i})") is False:
        crear_directorio(f"carpeta_nueva({i})")
        i = i + 1

"""
for i in range(317421):
    if i > 0:
        os.rmdir(f"carpeta_nueva({i})")
"""

print("-" * 50)