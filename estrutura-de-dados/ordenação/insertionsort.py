def insertionsort(lista):
    for i in range(1, len(lista)):
        escolhido = lista[i]
        j = i - 1
        while(j >= 0 and lista[j] > lista[i]):
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar
            j -= 1
            i -= 1
        lista[j+1] = escolhido
        
    return lista

L1= [5,2,9,7]
L2=[("Carlos",70),("João",20),("Cris", 40)]
print(insertionsort(L1))
print(insertionsort(L2))