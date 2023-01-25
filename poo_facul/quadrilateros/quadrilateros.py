class Quadrilateros():
    def __init__(self,lados):
        self._lados = lados
     
    @property
    def lados(self):
        
        return self._lados
    
    @lados.setter
    def lados(self,dado):
        self._lados = dado
    
    def calcular_area():
        pass
    
    def calcular_perimetro():
        pass
    
class Losango(Quadrilateros):
    def __init__(self, lados,diagonal_maior,diagonal_menor):
        super().__init__(lados)
        self._diagonal_maior = diagonal_maior
        self._diagonal_menor = diagonal_menor
        
    @property
    def diagonal_maior(self):
        return self._diagonal_maior
    
    @diagonal_maior.setter
    def diagonal_maior(self,dado):
        self._diagonal_maior = dado
        
    @property
    def diagonal_menor(self):
        return self._diagonal_menor
    
    @diagonal_menor.setter
    def diagonal_menor(self,dado):
        self._diagonal_menor = dado
        
    def calcular_area():
        pass
        
        
class Trapezio(Quadrilateros):
    def __init__(self, lados,altura):
        super().__init__(lados)
        self._altura = altura
        
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self,dado):
        self._altura = dado
        
    def calcular_area():
        pass