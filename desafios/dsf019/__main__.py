from funcionario import Gerente, Desenvolvedor, Designer

def main():
    dev = Desenvolvedor("Pedro", 5000)
    gerente = Gerente("Carlos", 8000)
    designer = Designer("Ana", 4000)

    print(f"{dev.nome}: R$ {dev.calcular_bonus():.2f}")
    print(f"{gerente.nome}: R$ {gerente.calcular_bonus():.2f}")
    print(f"{designer.nome}: R$ {designer.calcular_bonus():.2f}")

if __name__ == "__main__":
    main()
