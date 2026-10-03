from rich import print
from rich.panel import Panel

class Gamer:
    """Classe que representa um gamer com nome, nick e lista de jogos favoritos."""
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def adicionar_favorito(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos)

    def __rich__(self):
        favoritos_str = "\n".join(self.favoritos) if self.favoritos else "Nenhum jogo favorito."
        return Panel(
            f"[bold]Nome:[/bold] {self.nome}\n"
            f"[bold]Nick:[/bold] {self.nick}\n"
            f"[bold]Jogos Favoritos:[/bold]\n{favoritos_str}",
            title="Gamer",
            border_style="cyan",
            width=50
        )

j1 = Gamer("Pedro", "pedrogattosch")
j1.adicionar_favorito("The Witcher 3")
j1.adicionar_favorito("Cyberpunk 2077")
j1.adicionar_favorito("Elden Ring")

print(j1)
