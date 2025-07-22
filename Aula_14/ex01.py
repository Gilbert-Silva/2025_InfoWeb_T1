import enum
from datetime import datetime

class Pagamento(enum.Enum):
    EmAberto = 0
    PagoParcial = 1
    Pago = 2

class Boleto:
    def __init__(self, cod_barra, data_emissao, data_vencimento, valor):
        self.set_cod_barra(cod_barra)
        if cod_barra == "": raise ValueError("Código inválido")
        self.__cod_barra = cod_barra

        self.__data_emissao = data_emissao
        self.__data_vencimento = data_vencimento
        self.__data_pagamento = None
        self.set_data_pagamento(None)
        self.__valor_boleto = valor
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EmAberto    

    def set_data_pagamento(self, data_pagamento):
        if data_pagamento < datetime.now(): raise("Data inválida")

    def set_cod_barra(self, cod_barra):
        if cod_barra == "": raise ValueError("Código inválido")
        self.__cod_barra = cod_barra

    def pagar(self, valor_pago):
        self.__data_pagamento = datetime.now()
        if valor_pago <= 0: raise ValueError("Valor inválido")
        self.__valor_pago = valor_pago
        if valor_pago < self.__valor_boleto:
            self.__situacao_pagamento = Pagamento.PagoParcial
        if valor_pago == self.__valor_boleto:
            self.__situacao_pagamento = Pagamento.Pago

    def situacao(self):
        return self.__situacao_pagamento

x = Boleto(100)
print(x.situacao())
x.pagar(100)
print(x.situacao())


