from datetime import datetime, timedelta
import json

# Atributos - 6
# Encapsulamento - 6
# Validação - 6
# Init - 6
# Get - 6
# Set - 6
# Data_Entrega - 8
# Str - 6

class Emprestimo:
    def __init__(self, livro, data_emprestimo, periodo):
        self.set_livro(livro)
        self.set_data_emprestimo(data_emprestimo)
        self.set_periodo(periodo)
    def set_livro(self, livro):
        if livro == "": raise ValueError("Não pode ser vazio")
        self.__livro = livro
    def set_data_emprestimo(self, data_emprestimo):
        if data_emprestimo > datetime.now(): raise ValueError("Não pode ser no futuro")
        self.__data_emprestimo = data_emprestimo
    def set_periodo(self, periodo):
        if periodo < timedelta(0): raise ValueError("Não pode ser negativo")
        self.__periodo = periodo
    def get_livro(self): return self.__livro
    def get_data_emprestimo(self): return self.__data_emprestimo
    def get_periodo(self): return self.__periodo
    def data_devolucao(self): return self.__data_emprestimo + self.__periodo
    def __str__(self):
        return f"{self.__livro} {self.__data_emprestimo} {self.__periodo}"
    def to_json(self):
        dic = {}
        dic["livro"] = self.__livro
        dic["data_emprestimo"] = self.__data_emprestimo.strftime("%d/%m/%Y %H:%M")
        dic["periodo"] = f"{self.__periodo.days}-{self.__periodo.seconds}"
        return dic
                                                         
# Atributo - 5
# Main - 5
# Menu - 5
# Inserir - input - 5
# Inserir - conversão - 5
# Inserir - init - 5
# Inserir - append - 5
# Listar - 5
# Calcular - 10

class UI:
    __objetos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.calcular()
            if op == 4: cls.abrir()
            if op == 5: cls.salvar()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Calcular, 4-Abrir, 5-Salvar, 6-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        livro = input("Informe o livro: ")
        data_emprestimo = datetime.strptime(input("Informe a data de empréstimo: "), "%d/%m/%Y %H:%M")
        horas, minutos = map(int, input("Informe o período hh:mm: ").split(":"))
        periodo = timedelta(hours=horas, minutes=minutos)
        l = Emprestimo(livro, data_emprestimo, periodo)
        cls.__objetos.append(l)

    @classmethod
    def listar(cls):
        for l in cls.__objetos: print(l)

    @classmethod
    def calcular(cls):
        m = cls.__objetos[0]
        for t in cls.__objetos:
            if t.data_devolucao() < m.data_devolucao() : m = t
        print(m)

    @classmethod
    def abrir(cls):
        pass

    @classmethod
    def salvar(cls):
        with open("emprestimos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Emprestimo.to_json)

UI.main()



