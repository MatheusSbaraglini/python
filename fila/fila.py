import heapq

class FilaDePrioridade:

    def __init__(self):
        self.fila = []
        self.inidice = 0
    
    def inserir(self, item, prioridade):
        heapq.heappush(self.fila, (-prioridade, self.inidice, item))
        self.inidice += 1
    
    def remover(self):
        return heapq.heappop(self.fila)[-1]

class Item:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

fila = FilaDePrioridade()
fila.inserir(Item('matheus'), 26)
fila.inserir(Item('marina'), 27)
fila.inserir(Item('jacare'), 100)

print(fila.remover())
print(fila.remover())