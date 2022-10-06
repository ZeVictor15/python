class Cubo:
    
    def __init__(self,valor):
        self.valor = valor
        print("Objeto criado")
        
    def calcula_cubo(self):
        cubo = self.valor * self.valor
        return "O cubo é: " + str(cubo)
    
cubo = Cubo(10)
c = cubo.calcula_cubo()
print(c)