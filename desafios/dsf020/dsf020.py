class PDF:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self._extensao = ".pdf"
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        return self.nome + self._extensao

    def abrir(self):
        print(f"Abrindo PDF: {self.nome_completo}")


class DOC:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self._extensao = ".doc"
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        return self.nome + self._extensao

    def abrir(self):
        print(f"Abrindo DOC: {self.nome_completo}")


def abrir_arquivo(arquivo):
    arquivo.abrir()

pdf = PDF("trabalho", 15)
doc = DOC("relatorio", 8)

abrir_arquivo(pdf)
abrir_arquivo(doc)
