from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia=0):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return print(f"R${self.frete:.2f}")



class Caminhao(Transporte):
    fator = 1.2

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return print("A distância miníma é 50km.")
        else:
            self.frete = self.distancia * Caminhao.fator
            return print(f"R${self.frete:.2f}")


class Drone(Transporte):
    fator = 9.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia > 10:
            return print("A distância máxima é 10km.")
        else:
            self.frete = self.distancia * Drone.fator
            return print(f"R${self.frete:.2f}")
