import unittest

def classificar_numeros(lista):
    # Função ainda não implementada
    pass

class TestClassificarNumeros(unittest.TestCase):
    def test_classificar_numeros(self):
        self.assertEqual(classificar_numeros([6, 0, 2, 3, 5]), ["dadju", "nada", "par", "impar", "desconhecido"])
        self.assertEqual(classificar_numeros([12, 7, 4, 9, -3]), ["desconhecido", "desconhecido", "par", "impar", "impar"])
        self.assertEqual(classificar_numeros([8, 15, 0, 6, 2]), ["par", "impar", "nada", "dadju", "par"])
        
if __name__ == '__main__':
    unittest.main()
