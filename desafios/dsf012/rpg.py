from abc import ABC, abstractmethod
from random import choice, randint


class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca=100):
        golpe = choice(self.golpes)
        dano = randint(1, forca)

        print(f"{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com {golpe} de força {forca}")

        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nome} recebeu dano de {dano}!")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        golpes = [
            "Pulo Giratório",
            "Golpe de Espada",
            "Ataque Pesado"
        ]

        super().__init__(nome, vida, golpes)

    def curar(self):
        cura = randint(20, 100)
        self.vida += cura

        print(f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {cura} pontos de vida.")


class Mago(Personagem):
    def __init__(self, nome, vida):
        golpes = [
            "Magia Estática",
            "Bola de Fogo",
            "Raio Mágico"
        ]

        super().__init__(nome, vida, golpes)

    def curar(self):
        cura = randint(50, 150)
        self.vida += cura

        print(f"{self.nome} fez uma magia de cura e recuperou {cura} pontos de vida.")
