from aluno import Aluno, Pessoa

def main():
    a = Aluno("Pedro", 2005, "Engenharia")

    a.adicionar_curso("Medicina")

    print(a.__dict__)

if __name__ == "__main__":
    main()
