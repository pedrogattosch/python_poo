from hashlib import sha256
from pwinput import pwinput

class ContaBancaria:
    """Cria uma conta bancária com um número de conta, saldo e titular."""

    def __init__(self, numero_conta="", saldo=0, titular="", chave=None):
        self._numero_conta = numero_conta
        self.__saldo = saldo
        self._titular = titular

        if chave is None:
            chave = self.pede_senha()

        self.__hash = sha256(chave.encode()).hexdigest()

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def pede_senha(self):
        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break

        return senha

    def validar_senha(self, chave):
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.\n")
        else:
            print("Valor de depósito inválido.\n")

    def sacar(self, valor, chave=None):
        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if 0 < valor <= self.__saldo:
                self.__saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.\n")
            else:
                print("Saldo insuficiente ou valor inválido.\n")
        else:
            print(f"Senhã não confere. Saque negado.")

    def exibir_saldo(self):
        return f"Saldo atual: R${self.__saldo:.2f}\n"

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome:str=None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            self._titular = novo_nome
