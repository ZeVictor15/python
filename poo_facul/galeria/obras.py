from random import randint
class Obra:
    def __init__(self,dataAqui,titulo,tecnica,valor):
        self.dataAqui = dataAqui
        self.titulo = titulo
        self.tecnica = tecnica
        self.valor = valor
        self.autor = None
        self.codigo = __class__.geraCodigo()
        
    def __str__(self):
        return f'O código da obra é: {self.codigo}\nO titulo é: {self.titulo}\nO nome do autor é: {self.autor.nome}\nA tecnica usada foi: {self.tecnica} '
    
    def inserirAutor(self,artista):
        self.autor = artista
    
    def avaliar(self):
        self.valor = ((self.tecnica * 50) + (self.inovação * 80)) * 10
        print(self.valor)
    
    def imprimirObra(self):
        return f'O código é: {self.codigo}\nO titulo é {self.titulo} \nO valor é: {self.valor}'
    
    @staticmethod
    def geraCodigo():
        codigo = str(randint(1000,9999))
        return codigo
        
class Pintura(Obra) :
    def __init__(self, dataAqui, titulo, tecnica, valor,tipoTinta):
        super().__init__(dataAqui, titulo, tecnica, valor)
        self.tipoTinta = tipoTinta
    
    def __str__(self):
        return f'O código da pintura é: {self.codigo}\nO titulo é: {self.titulo}\nO nome do autor é: {self.autor.nome} \nA técnica usada foi: {self.tecnica} \nO tipo de tinta é: {self.tipoTinta}'
    
class Escultura(Obra):
    def __init__(self, dataAqui, titulo, tecnica, valor,tipoMate):
        super().__init__(dataAqui, titulo, tecnica, valor)
        self.tipoMate = tipoMate
        
    def __str__(self):
        return f'O código da Escultura é: {self.codigo}\nO titulo é: {self.titulo} \nO nome do autor é: {self.autor.nome} \nA técnica usada foi: {self.tecnica}\nO tipo de material é: {self.tipoMate}'


