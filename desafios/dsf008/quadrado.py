from poligono import Poligono

class Quadrado(Poligono):
    def __init__(self, comprimento_lado=0):
        super().__init__(4)
        self.comprimento_lado = comprimento_lado

    def perimetro(self):
        return print(f"Perímetro: {4*self.comprimento_lado}")

    def area(self):
        return print(f"Área: {self.comprimento_lado*self.comprimento_lado}")
