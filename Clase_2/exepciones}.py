lista = [1, 2]
try:
    print(lista[10])
except IndexError:
    print("Error de indice")