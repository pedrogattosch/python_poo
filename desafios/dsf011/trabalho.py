from abc import ABC, abstractmethod


class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome, sal_bruto=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        if self.salario < self.sal_min:
            print(f"{self.nome} recebe menos que um salário mínimo.")
        elif self.salario == self.sal_min:
            print(f"{self.nome} recebe exatamente um salário mínimo.")
        else:
            print(f"{self.nome} recebe mais que um salário mínimo.")


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab

        desconto_inss = self.sal_bruto * (self.inss / 100)

        self.salario = self.sal_bruto - desconto_inss

        return self.salario


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calc_sal(self):
        desconto_inss = self.sal_bruto * (self.inss / 100)

        self.salario = self.sal_bruto - desconto_inss

        return self.salario
