from funciones import quiz_1
import unittest


class test_1(unittest.TestCase):
    def calcular_mayor(self):
        lista_1 = [11, 22, 144, 200,555, 1010, 5, 777, 2019]
        mayor_test =quiz_1.N_mayor(lista_1)
        self.assertEqual(mayor_test, 2019)

    def calcular_menor(self):
        lista_2 = [200, 400, 800, 22, 11, 15, 155, 44, 89, 5, 2000, 678, 989]
        menor_test = quiz_1.N_mayor(lista_2)
        self.assertEqual(menor_test, 5)

if __name__ == '__main__':
    unittest.main()


