from filaTAD import Fila

def filaCres(fila1,fila2):
    fila3 = Fila()
    
    while not fila1.vazia() and not fila2.vazia():
        if fila1.cabeca.dado <= fila2.cabeca.dado:
            fila3.insere(fila1.remove())
        elif fila2.cabeca.dado < fila1.cabeca.dado:
            fila3.insere(fila2.remove())
    
    while (not fila1.vazia()):
        fila3.insere(fila1.remove())
    
    while (not fila2.vazia()):
        fila3.insere(fila2.remove())   
        
    return fila3

f1 = Fila()
f2 = Fila()
    
for i in range(3):
    f1.insere(input('Digite um valor para a fila 1: '))

    
for i in range(3):
    f2.insere(input('Digite um valor para a fila 2: '))
       
    
print(f1)   
print(f2) 
print(f1.cabeca.dado)
print(filaCres(f1,f2))