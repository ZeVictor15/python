class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s <- %s' % (self.anterior, self.dado)

class Pilha:
    def __init__(self):
        self.topo = None
        self._tamanho=0
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"
    
    def __len__(self):
        return self._tamanho
    
    def vazia(self):
        if self.topo == None:
            return True
        else:
            return False
        
    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo
        self._tamanho+=1
        
    def remove(self):
        if(self.vazia()):
            print("Impossível remover valor de pilha vazia.")
        else:
            self._tamanho-=1
            removido=self.topo.dado
            self.topo = self.topo.anterior
            return removido
    
    def compara_pilha(self,pilha):
        if len(self) != len(pilha):
            return False
        else:
            no_atual1 = self.topo
            no_atual2 = pilha.topo
            while no_atual1 != None:
                if no_atual1.dado != no_atual2.dado:
                    return False
                no_atual1 = no_atual1.anterior
                no_atual2 = no_atual2.anterior
            return True