from filaTAD import Fila

def comparaFila(fila1,fila2):
    if len(fila1) != len(fila2):
        return False
    else:
        cabeAtual1 = fila1.cabeca
        cabeAtual2 = fila2.cabeca
        
        while cabeAtual1 != None:
            if cabeAtual1.dado != cabeAtual2.dado:
                return False

            cabeAtual1 = cabeAtual1.proximo
            cabeAtual2 = cabeAtual2.proximo

        return True


def imparFilas(fila):
    fila2 = Fila()
    
    while not fila.vazia():
        if fila.cabeca.dado % 2 != 0:
            fila2.insere(fila.remove())
        else:
            fila.remove()
    return fila2


def imparImutavel(fila):
    flag = 0
    cabeca = fila.cabeca
    while cabeca != None:
        if cabeca.dado % 2 != 0:
            flag += 1
            
        cabeca = cabeca.proximo
        
    return flag

def parFilas(fila):
    flag = 0
    cabeca = fila.cabeca
    while cabeca != None:
        if cabeca.dado % 2 == 0:
            flag += 1
            
        cabeca = cabeca.proximo
        
    return flag




f1 = Fila()
f2 = Fila()

f1.insere(2)
f1.insere(3)
f1.insere(2)
f1.insere(3)
f1.insere(3)


f2.insere(2)
f2.insere(2)


print(imparImutavel(f1))
print(parFilas(f1))