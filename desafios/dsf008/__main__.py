from quadrado import Quadrado
from circulo import Circulo

def main():
    q1 = Quadrado(5)
    q1.area()
    q1.perimetro()

    c1 = Circulo(5)
    c1.area()
    c1.perimetro()

if __name__ == "__main__":
    main()
