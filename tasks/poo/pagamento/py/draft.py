from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass

class MetodoPix(MetodoPagamento):
    def __init__(self, chave: str):
        self.__chave = chave

    
    def processar_pagamento(self, valor: float):
        print(f"pagando chave: {self.chave}, valor {valor} com pix")

class Pagamento:
    def __init__(self, valor: float, descricao: str, metodo: MetodoPagamento):
        self.__valor: float = valor
        self.__descricao: str = descricao
        self.__metodo = metodo

    def pagar(self):
        self.__metodo.processar_pagamento(self.__valor)

        
    
