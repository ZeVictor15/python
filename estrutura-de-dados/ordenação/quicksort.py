def quickSort(lista, inicio, fim):
    if inicio < fim:
        pi = particao(lista, inicio, fim)
        quickSort(lista, inicio, pi - 1)
        quickSort(lista, pi + 1, fim)
 
def particao(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1
 
L1= [5,2,9,7]
L2=[("Carlos",70),("João",20),("Cris", 40)]
size1 = len(L1)
size2 = len(L2)
quickSort(L1, 0, size1 -1)
quickSort(L2, 0, size2 -1)

print(L1)
print(L2)
 

 

 
