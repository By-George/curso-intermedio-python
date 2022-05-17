#manjeo de excepcion cuando creamos un directorio

import os


try:
    os.mkdir("carpeta_prueba")
except FileExistsError as FEerror:
    print("Error ese directorio ya existe", FEerror)

print("=" * 50)