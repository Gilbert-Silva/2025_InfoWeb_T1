a = int(input("Digite um número: "))

print(b)

x = [1, 2, 4]
#print(x[5])

y = { "RN": "Natal"}
#print(y["PB"])

class MeuError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

x = MeuError("Teste")
raise x


