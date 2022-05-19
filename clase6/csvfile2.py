import csv
import os

def crear_directorio(ruta):
    try:
        os.mkdir(ruta)
    except FileExistsError as FEerror:
        pass    
    except FileNotFoundError as ex:
        print("No se encontro el directorio proporcionado")
    except Exception as ex:
        print("oops ocurrio un error")

    
""""
def agregar_datos(ruta,datos):
    with open("\\" + row['Platform'] + "\\" + row['Year'] + "\\videogames.txt", "w") as archivo:
        archivo.write(row)
"""

# id | Rank | Name | Platform | Year | Genre | Publisher | NA_Sales | EU_Sales | JP_Sales | Other_Sales

# Estructura de directorios

# Plataforma / Year / archivo.txt
# Nintendo/2000/videogames.txt
# en el archivo debe de ir el contenido de esa plataforma y ese año
ruta_inicial = "clase6\\csv\\"
with open('console_games.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ruta = ruta_inicial + row['Platform']
        if row['Platform'] == '':
            ruta = ruta_inicial + "Otras"
        print(ruta)
        crear_directorio(ruta)
        ruta += "\\" + row['Year']
        crear_directorio(ruta)
        with open(ruta + "\\videogames.txt", "a") as archivo:
            datos = f"{row['id']} | {row['Rank']} | {row['Name']}s | {row['Platform']} | {row['Year']} | {row['Genre']} | {row['Publisher']} | {row['NA_Sales']} | {row['EU_Sales']} | {row['JP_Sales']} | {row['Other_Sales']}\n"
            archivo.write(datos)