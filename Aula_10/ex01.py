class Aluno:
    def __init__(self, nome, matricula):           # construtor
        # if len(nome) < 3: raise ValueError("Nome inválido")
        # self.__nome = nome
        # if len(matricula) != 14: raise ValueError("Matrícula inválida")
        # self.__matricula = matricula
        self.set_nome(nome)
        self.set_matricula(matricula)
    def set_nome(self, nome):
        if len(nome) < 3: raise ValueError("Nome inválido")
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_matricula(self, matricula):
        if len(matricula) != 14: raise ValueError("Matrícula inválida")
        self.__matricula = matricula
    def get_matricula(self):
        return self.__matricula   
    def __str__(self):
        return f"Aluno(a) - Nome: {self.__nome} Matrícula: {self.__matricula}"

x = Aluno("Eduardo", "01234567890123")
print(x)
x.set_nome("Gilbert")
x.set_matricula("01234567890000")
print(x.get_nome())
print(x.get_matricula())
print(x)
