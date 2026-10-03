from banco import ContaBancaria

def main():
    c1 = ContaBancaria(111, 10000, "Pedro", "123456")

    c1.sacar(500)

    print(c1)

    c1.nome = "Teste"

if __name__ == "__main__":
    main()
