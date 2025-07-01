class Produto:
    def __init__(self, nome, preco, qtd):   # atributos - 10
        self.__nome = ""                    # validação - 10
        self.__preco = 0                    # encapsulamento - 10
        self.__quantidade = 0               # get - 10
        self.set_nome(nome)                 # set - 10
        self.set_preco(preco)               # cálculo - 10
        self.set_quantidade(qtd)

    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome
    def set_preco(self, preco):
        if preco <= 0: raise ValueError()
        self.__preco = preco
    def set_quantidade(self, quantidade):
        if quantidade <= 0: raise ValueError()
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_quantidade(self):
        return self.__quantidade
    
    def total(self):
        if self.__quantidade <= 10: return self.__quantidade * self.__preco
        if self.__quantidade <= 20: return self.__quantidade * self.__preco * 95 / 100
        return self.__quantidade * self.__preco * 90 / 100

    def __str__(self):
        return f"{self.__nome} {self.__preco} {self.__quantidade}"

                                      # sintaxe   - 10
class ProdutoUI:                      # main      - 5
    @staticmethod                     # menu      - 5
    def main():                       # inputs    - 5
        op = 0                        # instância - 5
        while op != 2:                # print     - 5
            op = ProdutoUI.menu()     # cálculo   - 5
            if op == 1: ProdutoUI.calculo()

    @staticmethod
    def menu():
        print("Escolha uma opção")
        return int(input("1 - Produto, 2 - Fim: "))
    
    @staticmethod
    def calculo():
        nome = input("Informe o nome: ")
        preco = float(input("Informe o preço: "))              
        qtd = int(input("Informe a quantidade: ")) 
        x = Produto(nome, preco, qtd)
        print(x)
        print(x.total())

ProdutoUI.main()