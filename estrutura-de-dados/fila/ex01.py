import sys
from filaTAD import Fila

sys.path.insert(0,'d:\\python\\estrutura-de-dados\\pilha')

from PilhaTAD import Pilha

def inverteFila(fila):
    pilha = Pilha()
    
    while (not fila.vazia()):
        pilha.insere(fila.remove())
    
    while (not pilha.vazia()):
        fila.insere(pilha.remove())
        
    return fila
    
fila = Fila()

for i in range(5):
    valor = input('Digite um valor para adicionar na lista: ')
    fila.insere(valor)

print(f'Esse são os valores da lista e os valores invertidos:\n {fila}\n {inverteFila(fila)}')


