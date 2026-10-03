from rich import print
from rich.panel import Panel

class Produto:
    """Classe que representa um produto com nome e preço do produto."""

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __rich__(self):
        return Panel(
            f"Produto: {self.nome}\n"
            f"Preço: R${self.preco:.2f}",
            title="Produto",
            border_style="green",
            width=40)

p1 = Produto("Notebook", 3500.00)
p2 = Produto("Smartphone", 1500.00)

print(p1)
print(p2)
