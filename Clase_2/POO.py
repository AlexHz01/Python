
# class es una palabra reservada que nos permite crear un nuevo tipo de dato
# Clases (sus elementos son opcionales)
# -Prpiedads
# -Constructor
# -Metodos

class Persona:
    # Atruibutos o propiedades (son lo mismo) de la clase (objetos)
    nombre = ""
    edad = 0
    pais = ""

    def __init__(self, nombre, edad,pais): # constructor
        self.nombre = nombre
        self.edad = edad
        self.pais = pais


    # def es un metodo
    def saludar(self):
        print("Hola soy {} y tengo {} años".format(self.nombre, self.edad))

    def despedirse(self):
        print("Adios")

    def comprar(self):
        self.saludar()
        print("Estoy comprando")
# persona = Persona("Enrique", 24, "Mexico")
# print(persona.nombre, persona.edad, persona.pais)
# persona.saludar()

class Empleado:
    trabajo = ""

class Estudiante(Persona, Empleado):
    escuela = ""


estudiante = Estudiante("Enrique", 24, "Mexico")
print(estudiante.nombre, estudiante.edad, estudiante.pais)
estudiante.comprar()
