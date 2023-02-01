def selectionsort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista

L1= [5,2,9,7]
L2=[("Carlos",70),("João",20),("Cris", 40)]
print(selectionsort(L1))
print(selectionsort(L2))