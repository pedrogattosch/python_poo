# Classe
class Pessoa:
    def __init__(self, n="", i=0): # Construtor
        # Atributos
        self.nome = n
        self.idade = i

    # Métodos
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


p1 = Pessoa("João", 30) # Instância

p1.aniversario() # Chamada do método aniversario
p1.mensagem() # Chamada do método mensagem
