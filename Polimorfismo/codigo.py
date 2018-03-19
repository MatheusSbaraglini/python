import math

class Forma():

    def __init__(self):
        print('construtor da forma')
    
    def area(self):
        print('area da forma')
    
    def perimetro(self):
        print('perimetro da forma')
    
    def descricao(self):
        print('descrição da forma')

class Quadrado(Forma):
    pass

    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4

class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.raio

'''
q = Quadrado(2)
print(q.area())
print(q.perimetro())'''

c = Circulo(3)
print(c.area())
print(c.perimetro())