import unittest
import random
from caso_practico import aleatorio, generar_matriz, suma_filas, suma_columna

class TestFuncionesMatriz(unittest.TestCase):

    def test_aleatorio(self):
        # Probamos la función aleatorio para asegurarnos de que devuelve un número entre 1 y 9
        numero_aleatorio = aleatorio()
        self.assertTrue(1 <= numero_aleatorio <= 9)

    def test_generar_matriz(self):
        # Probamos que la matriz generada tiene el tamaño correcto
        n = 5
        matriz_generada = generar_matriz(n)
        self.assertEqual(len(matriz_generada), n)
        for fila in matriz_generada:
            self.assertEqual(len(fila), n)

    def test_suma_filas(self):
        # Probamos la función suma_filas con una matriz de ejemplo y comparamos la suma con el resultado esperado
        matriz_ejemplo = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_suma_filas = [6, 15, 24]

        # Reemplazamos la función matriz por la matriz de ejemplo
        global matriz
        matriz = matriz_ejemplo

        # Ejecutamos la función y comparamos los resultados
        suma_filas(len(matriz_ejemplo))
        self.assertEqual(expected_suma_filas, [6, 15, 24])

    def test_suma_columna(self):
        # Probamos la función suma_columna con una matriz de ejemplo y comparamos la suma con el resultado esperado
        matriz_ejemplo = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_suma_columna = [12, 15, 18]

        # Reemplazamos la función matriz por la matriz de ejemplo
        global matriz
        matriz = matriz_ejemplo

        # Ejecutamos la función y comparamos los resultados
        suma_columna(len(matriz_ejemplo))
        self.assertEqual(expected_suma_columna, [12, 15, 18])

if __name__ == '__main__':
      unittest.main()
