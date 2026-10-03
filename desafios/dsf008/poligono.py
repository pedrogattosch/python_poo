from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados=3):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass
