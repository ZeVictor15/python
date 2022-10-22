class Nodo:
    def __init__(self, dado = 0, proximo_nodo = None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return ' %s -> %s' % (self.dado,self.proximo)

class Lista:
    def __init__(self):
        self.cabeca = None
        self.cauda  = None
        self._tamanho = 0

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def __len__(self):
        return self._tamanho

    def vazia(self):
        if self.cabeca == None:
            return True
        else: 
            return False

    def insereInicio(self,novoDado):
        novoNodo = Nodo(novoDado)
        if self.vazia():
            self.cabeca = novoNodo
            self.cauda  = novoDado
        else:
            novoNodo.proximo = self.cabeca
            self.cabeca = novoNodo

        self._tamanho += 1
    
    def insereFim(self,novoDado):
        novoNodo = Nodo(novoDado)
        if self.vazia():
            self.cabeca = novoNodo
            self.cauda  = novoDado
        else:
            self.cauda.proximo = novoDado
            self.cauda = novoNodo
        self._tamanho += 1

    def remove(self,posi):
        if self.vazia():
            print('Lista vazia')
        elif posi == 0:
            removido = self.cabeca.dado
            self.cabeca = self.cabeca.proximo
            if self.cabeca == None:
                self.cauda = None
        else:
            aux = 0
            if posi >= self.len():
                return "Posição invalida"
            else:
                while aux != posi:
                    nodoAnterior = nodoAtual
                    nodoAtual = nodoAtual.proximo
                
        self._tamanho -= 1
        return removido

    def busca(self,dado):
        if self.vazia():
            print('Lista vazia')

lista = Lista()
lista.insereInicio(5)
lista.insereFim(2)
print(lista.cabeca)
