class Nodo:
    def __init__(self, dado = None, cor = None, proximo_dado=None):
        self.dado = dado
        self.proximo = proximo_dado
        self.cor = cor
        
    def __repr__(self) -> str:
        return '%s %s -> %s' %(self.dado, self.cor, self.proximo)
    
class Lista:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        
    def __repr__(self):
        return '[ ' + str(self.cabeca) + ' ]'

    def __len__(self):
        return self.tamanho
    
    def vazia(self):
        if self.cabeca == None:
            return True
        else:
            return False

    def inserir_fim(self, novo_nodo):
        self.cauda.proximo = novo_nodo
        self.cauda = novo_nodo
        self.tamanho += 1
    
    def inserir(self, novo_dado, cor):
            novo_nodo = Nodo(novo_dado, cor)
            if self.vazia():
                self.cabeca = novo_nodo
                self.cauda = novo_nodo
                self.tamanho += 1
            else:
                if cor == 'V':
                    self.inserir_fim(novo_nodo)
                else:
                    self.inserir_prioridade(novo_nodo)
                
    def inserir_prioridade(self, novo_nodo):
        if self.cabeca.cor == 'V':
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
        else:
            aux = self.cabeca
            while aux.cor == 'A':
                ant = aux
                aux = aux.proximo
            novo_nodo.proximo = ant.proximo
            ant.proximo = novo_nodo
        self.tamanho += 1

lista = Lista()
lista.inserir(10,'V')
lista.inserir(11,'V')
lista.inserir(5,'A')
lista.inserir(12,'V')
lista.inserir(6,'A')
print(lista)