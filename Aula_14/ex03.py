import enum

class SituacaoMatricula(enum.Enum):
    Matriculado = 1
    Aprovado = 2
    Reprovado = 3
    ReprovadoPorFalta = 4
    Cancelado = 5
    Trancado = 6

class EstadoCivil(enum.Enum):
    Solteiro = 1
    Casado = 2
    Viuvo = 3
    Divorciado = 4

class Aluno:
    def __init__(self, nome, estado_civil):
        self.__nome = nome
        self.__estado_civil = estado_civil
        self.__situacao = SituacaoMatricula.Matriculado
    def cancelar_matricula(self):
        self.__situacao = SituacaoMatricula.Cancelado
    def trancar_matricula(self):
        self.__situacao = SituacaoMatricula.Trancado
    def __str__(self):
        return f"{self.__nome} - {self.__estado_civil} - {self.__situacao}"

# inserir
nome = input("Informe seu nome: ")
x = int(input("1-Solteiro, 2-Casado, 3-Viuvo, 4-Divorciado: "))
a = Aluno(nome, EstadoCivil(x))

# listar
print(a)

