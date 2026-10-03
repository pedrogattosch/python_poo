from rich import print
from rich.panel import Panel

class ContaBancaria:
    """
    Cria uma conta bancária com um número de conta, saldo e titular.

    Atributos:
        numero_conta (str): O número da conta bancária.
        saldo (float): O saldo atual da conta.
        titular (str): O nome do titular da conta.

    Métodos:
        depositar(valor): Adiciona um valor ao saldo da conta.
        sacar(valor): Subtrai um valor do saldo da conta, se houver saldo suficiente.
        exibir_saldo(): Retorna o saldo atual da conta.
    """

    def __init__(self, numero_conta="", saldo=0, titular=""):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular

    def __rich__(self):
        return Panel(
            f"[bold]Conta:[/bold] {self.numero_conta}\n"
            f"[bold]Titular:[/bold] {self.titular}\n"
            f"[bold]Saldo:[/bold] [green]R${self.saldo:.2f}[/green]",
            title="Conta Bancária"
        )

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de [bold green]R${valor:.2f}[/bold green] realizado com sucesso.\n")
        else:
            print("Valor de depósito inválido.\n")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de [bold red]R${valor:.2f}[/bold red] realizado com sucesso.\n")
        else:
            print("Saldo insuficiente ou valor inválido.\n")

    def exibir_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}\n"


c1 = ContaBancaria("12345-6", 1000, "Pedro Miguel")
print(c1)

c1.depositar(500)
c1.sacar(200)
print(c1.exibir_saldo())

