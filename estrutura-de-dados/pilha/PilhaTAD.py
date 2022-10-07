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
        
        if(self.topo==None):
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
    
    def compara_pilha(self,pilha1,pilha2):
        flag = True
        
        if len(pilha1) != len(pilha2):
            flag = False
            return flag
            
        while len(pilha1):
            if self.pilha1.topo == self.pilha2.topo:
                pilha1.remove()
                pilha2.remove()
            else:
                flag = False
                break

stack1 = Pilha()
stack2 = Pilha()
stack1.insere(5)
stack1.insere(23)
stack1.insere(32)

stack2.insere(5)
stack2.insere(23)
stack2.insere(32)

compara = Pilha()

compara.compara_pilha(stack1,stack2)


