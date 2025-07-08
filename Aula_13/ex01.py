from datetime import datetime
from enum import Enum

class Dias(Enum):
    Segunda = 0,
    Terça = 1,
    Quarta = 2,
    Quinta = 3,
    Sexta = 4,
    Sabado = 5,
    Domingo = 6

x = Dias.Terça
print(x)
print(type(x))    

dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

x = datetime(2025, 7, 8)
print(x)
hoje = datetime.now()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(dias[hoje.weekday()])
print(Dias(hoje.weekday()))

d = input("Informe a data de nascimento: ")
print(type(d))

dn = datetime.strptime(d, "%d/%m/%Y")
print(dn)
print(dias[dn.weekday()])
print(type(dn))

tempo = hoje - dn
print(tempo)
print(tempo.days // 365, "anos")
print(tempo.days % 365 // 30, "meses")
print(tempo.days % 365 % 30, "dias")









