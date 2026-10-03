class Diario:
    def __init__(self, senha="12345"):
        self.__segredos = []
        self.__senha = senha.strip()

    def escrever(self, mensagem):
        if isinstance(mensagem, str) and len(mensagem) > 0:
            self.__segredos.append(mensagem)

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha inválida!")
        else:
            print("Diário liberado!")
            for segredo in self.__segredos:
                print(segredo)

    @property
    def senha(self):
        raise PermissionError("A senha não é visível.")
