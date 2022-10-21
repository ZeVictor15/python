from filaTAD import Fila

def lerInteiros(qtd):
    fila = Fila()
    for i in range(int(qtd)):
        valor = input('Digite um número inteiro: ')
        fila.insere(valor)
    
    return fila

def quantidade():
   qtd = input(f'Digite a quantidade de inteiros para a fila: ')
   return qtd

fila1 = lerInteiros(quantidade())
fila2 = lerInteiros(quantidade())
fila3 = lerInteiros(quantidade())

fila4 = Fila()

print('-'*55)

print(f'Elementos da fila 1: {fila1}\nElementos da fila 2: {fila2}\nElementos da fila 3: {fila3}')

while not fila1.vazia() or not fila2.vazia or not fila3.vazia():
    
    if not fila1.vazia():
        dicionario = ('1', fila1.remove()) 
        fila4.insere(dicionario)
        
    if not fila2.vazia():
        dicionario = ('2', fila2.remove()) 
        fila4.insere(dicionario)
        
    if not fila3.vazia():
        dicionario = ('3', fila3.remove()) 
        fila4.insere(dicionario)

print('-'*55)
print(f'O fluxo da fila de canal é:\n{fila4}') 

