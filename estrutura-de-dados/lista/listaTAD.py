class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
    
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

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
        
    def insereInicio(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda  = novo_nodo
        else:
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
        self.tamanho += 1
            
    def insereFim(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo
        self.tamanho += 1
            
    def remove(self, posicao):
        if self.vazia():
            return "Impossível remover.Lista vazia."
        elif posicao == 0: 
            removido = self.cabeca.dado
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return removido
        else:
            aux = 0
            if posicao >= len(self):
                return "Posição inválida."
            else:
                nodo_atual = self.cabeca
                while aux != posicao:
                    nodo_anterior = nodo_atual
                    nodo_atual = nodo_atual.proximo
                    aux += 1
                removido = nodo_atual.dado

            if nodo_atual == self.cauda:
                self.cauda = nodo_anterior
            nodo_anterior.proximo =nodo_atual.proximo
            self.tamanho -= 1
            
            return removido
    
    def busca(self, dado):
        if self.vazia():
            return "Elemento não existe."
        else:
            nodo_atual = self.cabeca
            for i in range(len(self)):
                if nodo_atual.dado != dado:
                    nodo_atual = nodo_atual.proximo
                else:
                    return i
            return "Elemento não encontrado"

lista = Lista()
lista.insereFim(10)
lista.insereFim(12)
lista.insereFim(43)
print(lista.remove(lista.busca(43)))
print(lista)
