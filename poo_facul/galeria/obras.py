class Obra:
    def __init__(self,dataAqui,titulo,tecnica,artista):
        self.dataAqui = dataAqui
        self.titulo = titulo
        self.tecnica = tecnica
        self.autor = artista
        
    def __str__(self):
        pass
    
    def avaliar():
        pass
    
    def imprimirObra():
        pass

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