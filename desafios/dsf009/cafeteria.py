from abc import ABC, abstractmethod

class BebidaQuente:
    def preparar(self):
       print("--- Iniciando o preparo ---")
       self.ferver_agua()
       self.misturar()
       self.servir()
       print("Bebida pronta!\n")

    def ferver_agua(self):
        print("1. Fervendo a água")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando a água pelo pó de café.")

    def servir(self):
        print("3. Servindo em xícara pequena.")


class Cha(BebidaQuente):
    def misturar(self):
        print("2. Mergulhando o sachê na água quente.")

    def servir(self):
        print("3. Servindo na caneca de porcelana.")
