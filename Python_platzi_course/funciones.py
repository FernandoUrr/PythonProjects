import unittest
#Pruebas de caja negra
# def suma(num_1, num_2):
#     return num_1 + num_2



# class CajaNegraTest(unittest.TestCase):
#     def test_suma_dos_positivos(self):
#         num_1 = 10
#         num_2 = 5
        
#         resultado = suma(num_1, num_2)
#         self.assertEqual(resultado, 15)


#Manejo de excepciones
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i/ divisor for i in lista]
    except ZeroDivisionError as e:
        return lista

lista = list (range(10))
divisor = 2

print(divide_elementos_de_lista(lista, divisor))

# if __name__ == "__main__":
#     unittest.main()

