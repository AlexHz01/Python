print("Lista")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

# Las listas se pueden modificar, las tuplas no.
print("Lista modificada")
lista[0] = 100
print(lista)

print("valore diferentes")
lista3 = [1, "hola", True]
print(lista3)

print("modificar lista")
lista3[2] = False
lista3[1] = "adios"
print(lista3)

print("Agregar elementos a la lista")
lista3.append("nuevo")
print(lista3)

print("Combina dos listas")
lista.extend(lista3)
print(lista)

print("Eliminar elementos de la lista")
lista.remove(3)
print(lista)

lista.sort()
print(lista)