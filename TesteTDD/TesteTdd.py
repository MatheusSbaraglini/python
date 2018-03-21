import unittest
from calculadora import Calculadora

class TddExemplo(unittest.TestCase):

    def teste_soma(self):
        calc = Calculadora()
        result = calc.somar(10, 20)
        self.assertEqual(30, result)
    
    def teste_subtrair(self):
        calc = Calculadora()
        result = calc.subtrair(40, 20)
        self.assertEqual(20, result)


unittest.main()