import unittest

class ConverterNumeroRomano:

    def __init__(self):
        self.digito_map = {"M":1000,"D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

    def converter_para_decimal(self, numero_romano):
        val = 0
        for char in numero_romano:
            val += self.digito_map[char]
        return val


class TestConverterNumeroRomano(unittest.TestCase):

    def setUp(self):
        print('Construindo o objeto de conversão')
        self.cnr = ConverterNumeroRomano()
    
    def tearDown(self):
        print('Destruindo o objeto de conversão')
        self.cnr = None

    def test_mil(self):
        self.assertEqual(1001, self.cnr.converter_para_decimal('M'))
    
    def test_quinhentos(self):
        self.assertEqual(500, self.cnr.converter_para_decimal('D'))
    
    def test_cem(self):
        self.assertEqual(100, self.cnr.converter_para_decimal('C'))
    
    def test_dez(self):
        self.assertEqual(10, self.cnr.converter_para_decimal('X'))
    
    def test_vazio(self):
        self.assertTrue(self.cnr.converter_para_decimal('') == 0)


unittest.main()