from rich.console import Console
from rich.panel import Panel

console = Console()

class Mensagem:
    def __init__(self, mensagem):
        self._mensagem = mensagem
        self._tipo = ""
        self._icone = ""

    def mostrar(self):
        pass


class Alerta(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self._tipo = "ALERTA"
        self._icone = "⚠"

    def mostrar(self):
        painel = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo} {self._icone}",
            border_style="yellow",
            style="yellow"
        )

        console.print(painel)


class Erro(Mensagem):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self._tipo = "ERRO"
        self._icone = "⛔"

    def mostrar(self):
        painel = Panel(
            self._mensagem,
            title=f"{self._icone} {self._tipo} {self._icone}",
            border_style="red",
            style="red"
        )

        console.print(painel)


def main():
    Alerta("Esse curso é ótimo!").mostrar()
    Erro("Esse curso é ótimo!").mostrar()

if __name__ == "__main__":
    main()
