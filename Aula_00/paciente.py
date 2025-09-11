class Paciente:
    def __init__(self, nome, cpf, fone, nasc):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.nasc = nasc
    def __str__(self):
        return f"{self.nome} - {self.cpf}"    