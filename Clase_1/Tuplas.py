tupla = (1,2,3)
tupla2 = (1)

print(tupla)
print(tupla2)

tupla3 = (1, "hola", True)

print(tupla3[2])

# Tuplas con funciones

def enviar_datos():
    nombre = "jose"
    email = "jose@gmail.com"
    edad = 20
    return (nombre,email,edad)

def recibir_datos(datos):
    print(datos[0])
    print(datos[1])
    print(datos[2])

# datos = enviar_datos()

recibir_datos(enviar_datos())