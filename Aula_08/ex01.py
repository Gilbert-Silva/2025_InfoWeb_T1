class Agua:
    def __init__(self):  # Encapsulamento
        self.__mes = 1   # set get
        self.__ano = 2025
        self.__consumo = 0
    def set_mes(self, v):
        if v < 1 or v > 12: raise ValueError("O mês deve estar entre 1 e 12")
        self.__mes = v 
    def get_mes(self):
        return self.__mes       
    def set_ano(self, v):
        if v == 0: raise ValueError("O ano não pode ser 0")
        self.__ano = v 
    def get_ano(self):
        return self.__ano       
    def set_consumo(self, v):
        if v < 0: raise ValueError("O consumo não pode ser negativo")
        self.__consumo = v 
    def get_consumo(self):
        return self.__consumo       
    def valor(self):
        if self.__consumo <= 10: return 38
        if 11 <= self.__consumo <= 20: return 38 + (self.__consumo - 10) * 5
        if self.__consumo > 20: return 38 + 50 + (self.__consumo - 20) * 6  

class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2 

class UI:
    @staticmethod
    def menu():
        op = int(input("1-Água, 2-Triângulo, 9-Fim: "))
        return op
    
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.contaagua()
            if op == 2: UI.triangulo()

    @staticmethod
    def contaagua():    
        x = Agua()
        #print(f"Conta de água do mês {x.mes} do ano {x.ano}. Foi consumido é {x.consumo}")
        print(f"Conta de água do mês {x.get_mes()} do ano {x.get_ano()}. Foi consumido é {x.get_consumo()}")
        #x.mes = int(input("Informe o mês da conta: "))
        x.set_mes(int(input("Informe o mês da conta: ")))
        #x.ano = int(input("informe o ano: "))
        x.set_ano(int(input("informe o ano: ")))
        #x.consumo = int(input("informe o consumo em m3: "))
        x.set_consumo(int(input("informe o consumo em m3: ")))
        #print(f"O valor da conta de água do mês {x.mes} do ano {x.ano} é {x.valor()}")
        print(f"O valor da conta de água do mês {x.get_mes()} do ano {x.get_ano()} é {x.valor()}")
 
    @staticmethod
    def triangulo():    
        x = Triangulo()
        x.b = int(input("Informe o valor da base: "))
        x.h = int(input("Informe o valor da altura: "))
        print(f"A área do triângulo é {x.calc_area()}")

#p = UI()
#p.contaagua()
UI.main()
