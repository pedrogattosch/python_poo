from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError("Coloque um ano válido.")

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError("Não é permitido alterar a idade.")


class Aluno(Pessoa):
    cursos = ["Engenharia", "Administração", "Farmácia", "Direito"]

    def __init__(self, nome, nascimento, curso):
        super().__init__(nome, nascimento)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        pass

    @curso.setter
    def curso(self, curso):
        if curso not in Aluno.cursos:
            self._curso = None
            raise ValueError("O curso não está cadastrado.")
        else:
            self._curso = curso

    def adicionar_curso(self, curso):
        curso = curso.strip()
        Aluno.cursos.append(curso)
