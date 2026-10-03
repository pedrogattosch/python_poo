from credencial import Credencial

def main():
    c = Credencial()
    c.senha = "Pepo1910"
    print(c.senha)

    c.validar("Pepo1910")

if __name__ == "__main__":
    main()
