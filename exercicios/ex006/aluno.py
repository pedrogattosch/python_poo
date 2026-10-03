from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, curso, turma, nome, idade):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def matricular(self):
        pass
