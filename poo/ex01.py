class Ponto:
    def __init__(self,x,y,cor):
        self.x = x
        self.y = y
        self.cor = cor
        
    def mudaCor(self,novaCor):
        self.novaCor = novaCor
        
    def imprimir(self):
        print(f"A nova cor que você digitou é {self.novaCor}")
        
class Circunferencia:
    def __init__(self,ponto,raio,cor_linha,cor_prenchimento):
        self.centro = ponto
        self.raio = raio
        self.cor_linha = cor_linha
        self.cor_prenchimento = cor_prenchimento
        
    def area():
        pass
    
    def perimetro():
        pass
    
    def imprimir():
        pass
        