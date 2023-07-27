import random

class Matriz:
    def __init__(self, n):
        self.n = n
        self.matriz = self.generar_matriz()

    def aleatorio(self):
        return random.randint(1, 9)

    def generar_matriz(self):
        matriz = []
        for i in range(self.n):
            lista = [self.aleatorio() for _ in range(self.n)]
            matriz.append(lista)
        return matriz

    def imprimir_matriz(self):
        for fila in self.matriz:
            print(f"******* {'  '.join(map(str, fila))} ********")

    def suma_filas(self):
        lfila = []
        for fila in self.matriz:
            sfila = sum(fila)
            lfila.append(sfila)
        print("\nLa suma de cada fila es:", lfila)

    def suma_columnas(self):
        lcolumna = [[fila[i] for fila in self.matriz] for i in range(self.n)]
        lsuma = [sum(col) for col in lcolumna]
        print("\nLa suma de cada columna es:", lsuma)


if __name__ == '__main__':
    print("***************************************************")
    print("***************************************************")
    print("********* - SU MATRIZ CUADRADA A MEDIDA - *********")
    print("***************************************************")
    print("***************************************************\n")

    while True:
        try:
            numero = int(input("Introduzca un Número Entero Positivo: "))
            print("\n")
            if numero <= 0:
                continue
            break
        except ValueError:
            print("Es necesario un número entero, sin decimales por favor: ")

    matriz = Matriz(numero)
    matriz.imprimir_matriz()
    matriz.suma_filas()
    matriz.suma_columnas()
    input("\nPresiona Enter para salir...")
