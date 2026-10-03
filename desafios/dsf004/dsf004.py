from rich import print
import time

class Livro:
    """Classe que representa um livro com título, número de páginas e página atual."""
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

        print(f"Livro '{self.titulo}' tem {self.paginas} páginas. Você está na página {self.pagina_atual}.")

    def verificar_final(self):
        if self.pagina_atual >= self.paginas:
            print(f"Você chegou ao final do livro '{self.titulo}'.")
            return True
        else:
            return False

    def avancar_paginas(self, quantidade=1):
        c = 0
        for pag in range(0, quantidade, 1):
            if not self.verificar_final():
                self.pagina_atual += 1
                print(f"Página {self.pagina_atual} :arrow_forward:", end=" ")
                time.sleep(0.3)
                c += 1

            if self.verificar_final():
                break

        print(f"\nVocê avançou {c} página(s) no livro '{self.titulo}', você está na página {self.pagina_atual}.")

l1 = Livro("O Senhor dos Anéis", 30)
l1.avancar_paginas(10)
l1.avancar_paginas(25)

