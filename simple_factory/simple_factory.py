from abc import ABCMeta, abstractclassmethod


class Animal(metaclass=ABCMeta):

    @abstractclassmethod
    def falar(self):
        pass


class Cachorro(Animal):

    def falar(self):
        print('cachorro.falar')


class Gato(Animal):

    def falar(self):
        print('gato.falar')


class Factory:

    def produzir_som(self, object_type):
        return eval(object_type)().falar()


f = Factory()
f.produzir_som('Cachorro')
