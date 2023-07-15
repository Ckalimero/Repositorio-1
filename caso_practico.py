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

def suma_filas(n): #funcion suma listas y columnas, sin usar funcion sum(), ni tolist()
    x=0
    lfila=[]
    sfila=0
    while x<=(n-1):
        for i in range(len(matriz[x])):#Extraigo la fila
            sfila+=matriz[x][i]        #la sumo
        lfila.append(sfila)            #la añado a una lista que luego imprimo
        x+=1
        sfila=0
    print("La suma de cada fila es: ",lfila)

# funcion que extrae columnas con una lista por comprensión, las mete en otra lista y luego las suma e imprime
def suma_columna(numero):
    lcolumna=[]
    for i in range(len(matriz)):
        x=[fila[i] for fila in matriz]
        lcolumna.append(x)
    lsuma=[]
    for i in range(len(lcolumna)): # para la suma he usado la función sum(), es mucho más rápido
        y=sum(lcolumna[i])
        lsuma.append(y)             #sumo cada columna y el resultado lo meto en una lista que imprimo
    print("La suma de cada columan es: ",lsuma)


#pido al usuario que me de el nº para generar la matriz.Uso una excepción para validar que el nº sea entero
while True:
    try:
        numero=int(input("dame un numero: "))
        break
    except ValueError:
        print("Es necesario un numero entero, sin decimales por favor: ")
generar_matriz(numero)
suma_filas(numero)
suma_columna(numero)
