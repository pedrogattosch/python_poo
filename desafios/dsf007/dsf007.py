from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min = 1
    canal_max = 6
    volume_min = 0
    volume_max = 5

    def __init__(self, canal=1, volume=2):
        self.canal = canal
        self.volume = volume
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def avancar_canal(self):
        if self.ligado:
            if self.canal < ControleRemoto.canal_max:
                self.canal += 1
            else:
                self.canal = ControleRemoto.canal_min

    def retroceder_canal(self):
        if self.ligado:
            if self.canal > ControleRemoto.canal_min:
                self.canal -= 1
            else:
                self.canal = ControleRemoto.canal_max

    def aumentar_volume(self):
        if self.ligado:
            if self.volume < ControleRemoto.volume_max:
                self.volume += 1

    def diminuir_volume(self):
        if self.ligado:
            if self.volume > ControleRemoto.volume_min:
                self.volume -= 1

    def mostrar_tv(self):
        if not self.ligado:
            print(Panel(
                    "[bold red]A televisão está desligada.[/bold red]",
                    title="TV",
                    width=42
            ))
            return

        canais = ""

        for canal in range(self.canal_min, self.canal_max + 1):
            if canal == self.canal:
                canais += f"[black on yellow] {canal} [/black on yellow] "
            else:
                canais += f" {canal} "

        volume = ""

        for nivel in range(self.volume_max):
            if nivel < self.volume:
                volume += "[on dark_cyan]   [/]"
            else:
                volume += "[on grey]   [/]"

        conteudo = (
            f"[bold]CANAL  =[/bold] {canais}\n"
            f"[bold]VOLUME =[/bold] {volume}"
        )

        print(
            Panel(
                conteudo,
                title="TV",
                width=42
            )
        )



tv1 = ControleRemoto()

while True:
    tv1.mostrar_tv()
    comando = str(input("\n < CH > | - VOL + | @ LIGAR / DESLIGAR\n"))
    match comando:
        case "<":
            tv1.retroceder_canal()
        case ">":
            tv1.avancar_canal()
        case "-":
            tv1.diminuir_volume()
        case "+":
            tv1.aumentar_volume()
        case "@":
            if tv1.ligado:
                tv1.desligar()
            else:
                tv1.ligar()
        case "0":
            break
        case _:
            print("[bold red]Comando inválido![/bold red]")
