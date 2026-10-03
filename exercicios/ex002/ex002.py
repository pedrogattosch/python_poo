# Classe
class Pessoa:
    # Docstring
    """
    Classe Pessoa representa uma pessoa com nome e idade.

    Para criar uma instância da classe Pessoa:
    p1 = Pessoa("João", 30)
    """
    def __init__(self, nome="", idade=0): # Construtor
        # Atributos
        self.nome = nome
        self.idade = idade

    # Métodos
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Método especial para representar a instância como uma string
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


p1 = Pessoa("João", 30) # Instância

p1.aniversario() # Chamada do método aniversario
print(p1) # Chamada do método __str__ para exibir a mensagem

# Dunder atributes
print(p1.__doc__) # Exibe a docstring da classe Pessoa
print(p1.__dict__) # Exibe o dicionário de atributos da instância p1
print(p1.__class__) # Exibe a classe da instância p1

