class Nodo:
    def __init__(self, dado = 0, proximo_nodo = None, cor = None):
        self.dado = dado
        self.proximo = proximo_nodo
        self.cor = cor
    
    def __repr__(self):
        return '%s %s -> %s' % (self.dado,self.cor, self.proximo)

class Lista:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho=0
    
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def __len__(self):
        return self.tamanho

    def vazia(self):
        if(self.cabeca == None):
            return True
        else:
            return False

    def insereFim(self, novo_dado,cor):
        
        novo_nodo = Nodo(novo_dado)
        novo_nodo.cor = cor
        
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda  = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo
        
        self.tamanho+=1

    def insereInicio(self, novo_dado,cor):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.cor = cor
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda  = novo_nodo
        else:
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo

        self.tamanho+=1
        
    def inserir_prioridade(self, novo_dado,cor):
        novo_nodo = Nodo(novo_dado,cor)
        novo_nodo.cor = cor
        if cor == 'v':
            if self.vazia():
                self.cabeca = novo_nodo
                self.cauda  = novo_nodo
        else:
            ant = novo_nodo
            aux = ant.proximo
            while aux != None and aux == 'a':
                ant = aux
                aux = ant.proximo
            
            
            ant.proximo = novo_nodo
            novo_nodo.proximo = aux
            
                
            
         

lista = Lista()
lista.inserir_prioridade(13,'v')
lista.inserir_prioridade(5,'a')
lista.inserir_prioridade(4,'v')
lista.inserir_prioridade(6,'v')
print(lista)