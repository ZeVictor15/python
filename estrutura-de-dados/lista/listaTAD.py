class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
    
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class Lista:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho=0

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    def vazia(self):
        if(self.cabeca == None):
            return True
        else:
            return False
        
    def insereInicio(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            novo_nodo.proximo = self.cabeca
            self.cabeca =novo_nodo
            self.tamanho+=1
            
    def insereFim(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            self.cauda =novo_nodo
            self.tamanho+=1