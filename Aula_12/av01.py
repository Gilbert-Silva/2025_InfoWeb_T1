class Aluno:
    def __init__(self, nome, email, mat):   # atributos - 10
        self.__nome = ""                    # validação - 10
        self.__email = ""                   # encapsulamento - 10
        self.__matricula = ""               # get - 10
        self.set_nome(nome)                 # set - 10
        self.set_email(email)               # cálculo - 10
        self.set_matricula(mat)

    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError()
        self.__email = email
    def set_matricula(self, matricula):
        if len(matricula) != 14: raise ValueError()
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_matricula(self):
        return self.__matricula
    
    def ano_conclusao(self):
        return int(self.__matricula[:4]) + 4

    def __str__(self):
        return f"{self.__nome} {self.__email} {self.__matricula}"

                                    # sintaxe   - 10
class AlunoUI:                      # main      - 5
    @staticmethod                   # menu      - 5
    def main():                     # inputs    - 5
        op = 0                      # instância - 5
        while op != 2:              # print     - 5
            op = AlunoUI.menu()     # cálculo   - 5
            if op == 1: AlunoUI.calculo()

    @staticmethod
    def menu():
        print("Escolha uma opção")
        return int(input("1 - Aluno, 2 - Fim: "))
    
    @staticmethod
    def calculo():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")              
        mat = input("Informe a matrícula: ") 
        x = Aluno(nome, email, mat)
        print(x)
        print(x.ano_conclusao())

AlunoUI.main()