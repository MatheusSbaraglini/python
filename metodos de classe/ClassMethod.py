class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)
    
    @classmethod
    def de_string(cls, data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        data = cls(dia, mes, ano)
        print(data)

d = Data(10,10,10)
d1 = Data.de_string('10-10-2016')
print(d1)