from rich import print
from rich.panel import Panel

class Churrasco:
    """Classe que representa um churrasco e quantidade de convidados e calcular o custo total e a média por convidado."""
    consumo = 0.4
    preco = 82.40

    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def calcular_qtd_carne(self):
        return self.quantidade * Churrasco.consumo

    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * Churrasco.preco

    def calcular_media_por_convidado(self):
        return self.calcular_custo_total() / self.quantidade

    def analisar(self):
        custo_total = self.calcular_custo_total()
        media_por_convidado = self.calcular_media_por_convidado()

        return Panel(
            f"[bold]Churrasco:[/bold] {self.nome}\n"
            f"[bold]Quantidade de convidados:[/bold] {self.quantidade}\n"
            f"[bold]Custo total:[/bold] R${custo_total:.2f}\n"
            f"[bold]Média por convidado:[/bold] R${media_por_convidado:.2f}",
            title="Análise do churrasco",
            border_style="blue"
        )

c1 = Churrasco("Churrasco do Pedro", 15)
print(c1.analisar())
