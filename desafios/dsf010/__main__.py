from transportes import *

def main():
    entrega1 = Moto(20)
    entrega1.calcular_frete()

    entrega2 = Caminhao(60)
    entrega2.calcular_frete()

    entrega3 = Drone(11)
    entrega3.calcular_frete()

if __name__ == "__main__":
    main()
