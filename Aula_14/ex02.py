import enum
class SituacaoFarol(enum.Enum):
    Desligado = 0
    LuzBaixa = 1
    LuzAlta = 2

class Farol2:
    def __init__(self):
        self.__situacao = SituacaoFarol.Desligado
    def get_situacao(self):
        return self.__situacao
    def ligar_baixo(self):
        self.__situacao = SituacaoFarol.LuzBaixa
    def ligar_alto(self):
        self.__situacao = SituacaoFarol.LuzAlta
    def desligar(self):
        self.__situacao = SituacaoFarol.Desligado

class Farol:
    def __init__(self):
        self.__ligado = False
    def get_ligado(self):
        return self.__ligado
    def ligar(self):
        self.__ligado = True
    def desligar(self):
        self.__ligado = False

x = Farol()
print(x.get_ligado())
x.ligar()
print(x.get_ligado())
x.desligar()
print(x.get_ligado())

y = Farol2()
print(y.get_situacao())
y.ligar_baixo()
print(y.get_situacao())
y.ligar_alto()
print(y.get_situacao())
