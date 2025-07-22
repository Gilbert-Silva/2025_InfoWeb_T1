import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    
def salvar():
    a = Cliente(1, "Douglas Crockford")
    b = Cliente(2, "Jon Bosak")
    x = [a, b]
    with open("clientes.json", mode="w") as arquivo:
        json.dump(x, arquivo, default = vars)
    #arquivo.close()

def abrir():
    x = []
    with open("clientes.json", mode="r") as arquivo:
        lista = json.load(arquivo)
        for obj in lista:
            c = Cliente(obj["id"], obj["nome"])
            x.append(c)
    for c in x: print(c) 

abrir()
