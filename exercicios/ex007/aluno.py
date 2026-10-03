from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, curso, turma, nome, idade):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def matricular(self):
        pass

    def estudar(self):
        return print(f"{self.nome} está estudando na turma {self.turma}")
