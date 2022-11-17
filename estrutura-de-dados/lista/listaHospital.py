class Nodo:
    def __init__(self, dado = 0, cor = None, proximo_nodo = None,):
        self.dado = dado
        self.proximo = proximo_nodo
        self.cor = cor
    
    def __repr__(self):
        return '%s %s -> %s' % (self.dado,self.cor, self.proximo)

class Lista:
    def __init__(self):
        self.cabeca  = None
        self.cauda   = None
        self.tamanho = 0
    
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
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda  = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo
        
        self.tamanho+=1

    def insere(self, novo_dado,cor):
        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda  = novo_nodo
        else:
            if novo_nodo == 'v':
                self.insereFim(novo_nodo)
            else:
                self.inserir_prioridade(novo_dado)

        self.tamanho+=1
        
    def inserir_prioridade(self, novo_dado):
        if self.vazia():
                self.cabeca = novo_dado
                self.cauda  = novo_dado
        else: 
            if self.cabeca.cor == 'v':
                novo_dado.proximo = self.cabeca
                self.cabeca = novo_dado
            else:
                nodo_atual = self.cabeca
                while nodo_atual.cor != "v":
                    nodo_anterior = nodo_atual
                    nodo_atual = nodo_atual.proximo
                    
                novo_dado.proximo = nodo_atual
                nodo_anterior = novo_dado
               
            
lista = Lista()
lista.insere(10,'v')
lista.insere(11,'v')
lista.insere(5,'a')
lista.insere(12,'v')
lista.insere(6,'a')

print(lista)