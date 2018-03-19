from abc import ABCMeta, abstractmethod

class MinhaClassAbstrata(metaclass=ABCMeta):
    
    @abstractmethod
    def fazer_algo(self):
        pass
    
    @abstractmethod
    def fazer_algo_novamente(self, o_que_fazer):
        pass