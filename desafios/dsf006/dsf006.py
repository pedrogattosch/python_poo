from rich import print

class Caneta:
    def __init__(self):
        while True:
            escolha = input("Escolha a cor da caneta (azul, vermelha, verde): ").lower().strip()

            match escolha:
                case "azul":
                    self.cor = "[blue]"
                    break
                case "vermelha":
                    self.cor = "[red]"
                    break
                case "verde":
                    self.cor = "[green]"
                    break
                case _:
                    print("Opção inválida. Por favor, escolha uma cor válida (azul, vermelha, verde).")

        self.tamapada = True

    def destampar(self) -> bool:
        print(f"A caneta foi destampada.")
        self.tamapada = False

    def escrever(self, texto: str) -> None:
        if not self.tamapada:
            print(f"{self.cor}{texto}[/]")
        else:
            print(f"A caneta não pode escrever, é necessário destampar ela.")

c1 = Caneta()
c1.destampar()
c1.escrever("Olá, mundo!")
