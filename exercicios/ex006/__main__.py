from aluno import Aluno
from professor import Professor

def main():
    a1 = Aluno("Engenharia", "EC23", "Pedro", 21)
    a1.fazer_aniversario()

    p1 = Professor("Programação", 10000, "Ricardo", 38)
    p1.fazer_aniversario()
    p1.dar_aula()

if __name__ == "__main__":
    main()
