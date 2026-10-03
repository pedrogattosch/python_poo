from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, disciplina, salario, nome, idade):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

    def dar_aula(self):
        print(f"{self.nome} começou a aula.")
