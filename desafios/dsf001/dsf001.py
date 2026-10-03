class Funcionario:
    """Classe que representa um funcionário com nome, cargo e setor."""

    # Atributos de classe
    empresa = "Microsoft"  # Atributo de classe compartilhado por todas as instâncias

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def aposentar(self) -> str:
        return print(f"{self.nome} está se aposentando do cargo de {self.cargo} do setor {self.setor} na empresa {Funcionario.empresa}.\n")

    def __str__(self):
        return f"Funcionário: {self.nome}, Setor: {self.setor}, Cargo: {self.cargo}\n"

Funcionario.empresa = "Apple"

f1 = Funcionario("Carlos", "Financeiro", "Analista")
f1.aposentar()
