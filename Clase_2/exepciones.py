lista = [1, 2]
try:
    print(lista[1])
except IndexError:
    print("Error de indice")
else:
    print("Todo bien")

