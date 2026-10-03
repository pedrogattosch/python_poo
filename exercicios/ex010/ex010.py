class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Atributo validável
    @property
    def nota(self): # Getter
        return self._nota

    @nota.setter
    def nota(self, valor): # Setter
        if 0 <= valor <= 10:
            self._nota = valor
            return print(f"{self._nota}")
        else:
            return print("Informe um valor válido entre 0 e 10.")

    def __str__(self):
        return f"{self.__dict__}"

av1 = Avaliacao("Pedro", "Matemática", 9.5)
av1.nota = 8
print(av1)
