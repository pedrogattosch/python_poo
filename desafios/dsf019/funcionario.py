from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    @abstractmethod
    def calcular_bonus(self):
        pass


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.get_salario() * 0.10


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.get_salario() * 0.15


class Designer(Funcionario):
    def calcular_bonus(self):
        return self.get_salario() * 0.08
