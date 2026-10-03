from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self):
        self._valor = 0

    @property
    def fvalor(self):
        valor = f"{self._valor:,.2f}"
        return valor.replace(",", "X").replace(".", ",").replace("X", ".")

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def pagar(self):
        print(
            f"Pagamento CONFIRMADO de R$ {self.fvalor} via Boleto"
        )


class Pix(Pagamento):
    def pagar(self):
        print(
            f"Pagamento CONFIRMADO de R$ {self.fvalor} via PIX"
        )


class CartaoCredito(Pagamento):
    def pagar(self):
        print(
            f"Pagamento CONFIRMADO de R$ {self.fvalor} via Cartão de Crédito"
        )


def finalizar_compra(pagamento, valor):
    pagamento._valor = valor
    pagamento.pagar()


def main():
    finalizar_compra(CartaoCredito(), valor=25_324.20)

if __name__ == "__main__":
    main()
