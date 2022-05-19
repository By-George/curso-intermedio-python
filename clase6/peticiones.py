import requests
import os

os.system('cls')

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.json())

respuesta = response.json()

for key, value in respuesta.items():
    print(f"La clave es {key} y su contenido es {value}")