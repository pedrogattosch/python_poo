class Termostato:
    def __init__(self, temperatura=16):
        self.__temperatura = 16
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

        if valor % 0.5 != 0:
            raise ValueError("Temperatura inválida. Use incrementos de 0.5°C.")

    @property
    def ftemperatura(self):
        return f"{self.__temperatura:.1f}°C"


t1 = Termostato(25)
print(t1.ftemperatura)

t2 = Termostato()
t2.temperatura = 29.2
print(t2.ftemperatura)
