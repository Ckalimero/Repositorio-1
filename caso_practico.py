import random
#funcion que genera el número aleatorio entre 0 y 9 que luego se incluirá en cada celda de la matriz
def aleatorio():
    numero_aleatorio=random.randint(1,9)
    return numero_aleatorio

# función que genera la matriz de nxn con los números aleatorios que genera la función aleatorio() y la imprime
matriz=[]
def generar_matriz(n):
    for i in range(n):
        lista=[]
        for j in range(n):
            lista.append(aleatorio())
        matriz.append(lista)
    for fila in matriz:
        print(fila)

#pido al usuario que me de el número para generar la matriz de nxn, y llamo a la función para crear e imprimir la matriz
numero=int(input("dame un numero: "))
generar_matriz(numero)

def suma_filas():
    pass

def suma_columnas():
    pass