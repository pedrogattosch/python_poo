from abc import ABC, abstractmethod # ABC = Abrastract Base Classes

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} acabou de fazer {self.idade} anos!")

    @abstractmethod # Todas as classes precisam desse metódo abstrato
    def estudar(self):
        pass
