from trabalho import *

def main():
    f1 = Horista("Pedro", 20, 100)
    f2 = Mensalista("João", 3000)


    print(f"Salário de {f1.nome}: R$ {f1.calc_sal():.2f}")
    f1.analisar_sal()

    print(f"Salário de {f2.nome}: R$ {f2.calc_sal():.2f}")
    f2.analisar_sal()

if __name__ == "__main__":
    main()
