#pasar todo lo de monitor1 a un archivo txt
#crear una carpeta donde se almacenara los logs
#crear un archivo con X nombre
# insertar la informacion recabada en el archivo

import psutil
import os

os.mkdir(f"logs")

with open ("logs\log.txt","w") as archivo:
    #print(archivo.read())
    # nucles del cpu
    cpu_nucleos = psutil.cpu_count()
    cpu_frecuencia = psutil.cpu_freq()

    # memoria
    memoria_virtual = psutil.virtual_memory()

    # disco
    disco_uso = psutil.disk_usage('/')

    os.system('cls')

    archivo.write("=" * 50)

    archivo.write("\nInformacion del sistema \n")
    archivo.write(f"Nucleos del CPU =>  {cpu_nucleos}\n")
    archivo.write(f"Frecuenca del CPU => {cpu_frecuencia}\n")
    archivo.write(f"Memoria virutal => {memoria_virtual}\n")
    archivo.write(f"Uso de disco => {disco_uso}\n")
    archivo.write("=" * 50)

with open ("logs\log.txt") as archivo:
    print(archivo.read())