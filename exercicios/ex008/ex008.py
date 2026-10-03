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
        self.numero_conta = numero_conta # publico (+)
        self.__saldo = saldo # privado (-)
        self._titular = titular # protegido (#)

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.\n")
        else:
            print("Valor de depósito inválido.\n")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.\n")
        else:
            print("Saldo insuficiente ou valor inválido.\n")

    def exibir_saldo(self):
        return f"Saldo atual: R${self.__saldo:.2f}\n"


c1 = ContaBancaria("12345-6", 1000, "Pedro Miguel")
print(c1)

c1.depositar(500)
c1.sacar(200)

c1.titular = "João"
c1.saldo = 0

print(c1)

# NUNCA FAÇA ISSO
c1._titular = "Sofia"
c1._ContaBancaria__saldo = 0

print(c1)
