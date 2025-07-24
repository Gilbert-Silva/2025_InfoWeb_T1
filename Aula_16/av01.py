from datetime import datetime, timedelta

# Atributos - 6
# Encapsulamento - 6
# Validação - 6
# Init - 6
# Get - 6
# Set - 6
# Data_Entrega - 8
# Str - 6

class Tarefa:
    def __init__(self, descricao, data_inicio, duracao):
        self.set_descricao(descricao)
        self.set_data_inicio(data_inicio)
        self.set_duracao(duracao)
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Não pode ser vazio")
        self.__descricao = descricao
    def set_data_inicio(self, data_inicio):
        if data_inicio < datetime.now(): raise ValueError("Não pode ser no passado")
        self.__data_inicio = data_inicio
    def set_duracao(self, duracao):
        if duracao < timedelta(0): raise ValueError("Não pode ser negativo")
        self.__duracao = duracao
    def get_descricao(self): return self.__descricao
    def get_data_inicio(self): return self.__data_inicio
    def get_duracao(self): return self.__duracao
    def data_entrega(self): return self.__data_inicio + self.__duracao
    def __str__(self):
        return f"{self.__descricao} {self.__data_inicio} {self.__duracao}"
    
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
        while op != 4:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()
            if op == 3: cls.calcular()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Calcular, 4-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        descricao = input("Informe a descrição: ")
        data_inicio = datetime.strptime(input("Informe a data de início: "), "%d/%m/%Y %H:%M")
        horas, minutos = map(int, input("Informe a duração hh:mm: ").split(":"))
        duracao = timedelta(hours=horas, minutes=minutos)
        t = Tarefa(descricao, data_inicio, duracao)
        cls.__objetos.append(t)

    @classmethod
    def listar(cls):
        for t in cls.__objetos: print(t)

    @classmethod
    def calcular(cls):
        m = cls.__objetos[0]
        for t in cls.__objetos:
            if t.data_entrega() < m.data_entrega() : m = t
        print(m)

UI.main()



