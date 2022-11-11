import json

with open("archivo.json") as archivo:
    dato= json.load(archivo)

print(dato)
print(dato['nombres'][0]['apellido'])