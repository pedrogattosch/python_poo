from poligono import Poligono

class Circulo(Poligono):
    pi = 3.14

    def __init__(self, raio=0):
        super.__init__(0)
        self.raio = raio

    def perimetro(self):
        return print(f"Perímetro: {2*Circulo.pi*self.raio}")

    def area(self):
        return print(f"Área: {Circulo.pi*(self.raio*self.raio)}")
