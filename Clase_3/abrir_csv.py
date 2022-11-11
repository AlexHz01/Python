import csv

doc_csv = open('archivo.csv', 'w')
csv_data = csv.writer(doc_csv)
lista = [['nombre', 'apellido', 'edad'], ['Juan', 'Perez', '25'], ['Maria', 'Gomez', '30']]
# csv_data.writerows(lista)
for elemento in lista:
    csv_data.writerow(elemento)
doc_csv.close()

doc = open('archivo.csv', 'r')
documento = csv.reader(doc)
for(nombre, apellido, edad) in documento:
    print(nombre, apellido, edad)
doc.close()