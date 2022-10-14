from random import randint
class Obra:
    def __init__(self,dataAqui,titulo,tecnica,artista):
        self.dataAqui = dataAqui
        self.titulo = titulo
        self.tecnica = tecnica
        self.autor = artista
        self.codigo = __class__.geraCodigo()
        
    def __str__(self):
        return f'{self.codigo}'
    
    def avaliar(self):
        pass
    
    def imprimirObra(self):
        print(self.codigo)
    
    @staticmethod
    def geraCodigo():
        codigo = str(randint(1000,9999))
        return codigo
        
class Pintura(Obra) :
    def __init__(self, dataAqui, titulo, tecnica, artista,tipoTinta):
        super().__init__(dataAqui, titulo, tecnica, artista)
        self.tipoTinta = tipoTinta
    
    def __str__(self):
        return super().__str__()
    
class Escultura(Obra):
    def __init__(self, dataAqui, titulo, tecnica, artista,tipoMat):
        super().__init__(dataAqui, titulo, tecnica, artista)
        self.tipoMat = tipoMat 
        
    
o1= Obra(2,'victor','lapis','oden')
