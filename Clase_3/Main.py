def crear_archivo():
    archivo = open('datos.txt', 'w') ## w = write
    archivo.close()

def escribir_archivo():
    archivo = open('datos.txt', 'a') ## a = append
    archivo.write('Hola mundo\n')
    archivo.write('CURSO DE PYTHON')


def leer_archivo():
    archivo = open('datos.txt', 'r')  ## r = read
    linea = archivo.readline()
    while linea != '':
        print(linea)
        linea = archivo.readline()
    archivo.close()


crear_archivo()
escribir_archivo()
leer_archivo()