from random import randint
class Ingressos():
    def __init__(self,valor):
        self.valor  = valor
        self.status = 'Não vendido'
        self.codigo = __class__.codigo()
        
    def __str__(self):
        return f'O valor do ingresso é: {self.valor} o status do ingresso é: {self.status} o codigo do ingresso é: {self.codigo}'
    
    @staticmethod
    def codigo():
        codigo = str(randint(1000,99999))
        return codigo

class Camarote(Ingressos):
    def __init__(self, valor,valorAdi):
        super().__init__(valor)
        self.valorAdi = valorAdi
        self.valor = int(valor) + int(valorAdi)
        
        
    
