class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} acabou de fazer {self.idade} anos!")
