class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
        self._area = base * altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError("A base deve ser maior que zero.")

        self._base = valor
        self._area = self._base * self._altura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("A altura deve ser maior que zero.")

        self._altura = valor
        self._area = self._base * self._altura

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, valor):
        raise PermissionError("Não pode definir a área.")
