class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} acabou de fazer {self.idade} anos!")


class Aluno(Pessoa): # Pega os atributos e métodos da classe Pessoa
    def __init__(self, curso, turma, nome, idade):
        super().__init__(nome, idade) # Chama o construtor da superclasse Pessoa
        self.curso = curso
        self.turma = turma

    def matricular(self):
        pass


class Professor(Pessoa):
    def __init__(self, disciplina, salario, nome, idade):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

    def dar_aula(self):
        print(f"{self.nome} começou a aula.")

a1 = Aluno("Engenharia", "EC23", "Pedro", 21)
a1.fazer_aniversario()

p1 = Professor("Programação", 10000, "Ricardo", 38)
p1.fazer_aniversario()
p1.dar_aula()
