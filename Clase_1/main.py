nombre = "Enrique Alejandro"
age = 22
country = "Mexico"

print("hola yo me llamo {} y tengo {} años de edad y soy de {}".format(nombre, age, country))
print(type(nombre))
print(type(age))

name = input("Hla porfavor ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
ciudad = input("ingrese su pais: ")


if ciudad == "Mexico":
    print("Hola buenos dias {} usted tiene {} años y vive en {} es un placer tenerlo en nuestro equipo".format(name,edad,ciudad))
else:
    print("Hola sr. {} usted no es de Mexico no podemos aceptarlo en el equipo".format(name))


