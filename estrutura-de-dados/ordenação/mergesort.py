def mergesort(lista,inicio,fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergesort(lista,inicio,meio)
        mergesort(lista,meio+1 ,fim)
        unir(lista,inicio,meio,fim)
    
    return lista

def unir(lista,inicio,meio,fim):
    subesq = lista[inicio:meio]
    subdir = lista[meio:fim]
    i = 0
    j = 0
    for k in range(inicio,fim):
        if i >= len(subesq):
            lista[k] = subdir[j]
            j += 1
        elif j >= len(subdir):
            lista[k] = subesq[i]
            i += 1
        elif subesq[i] < subdir[j]:
            lista[k] = subesq[i]
            i += 1
        else:
            lista[k] = subdir[j]
            j += 1
        k += 1
        
L1= [5,2,9,7]
L2= [("Carlos",70),("João",20),("Cris", 40)]
size1 = len(L1)
size2 = len(L2)
mergesort(L1, 0, size1 -1)
mergesort(L2, 0, size2 -1)
print(L1)
print(L2)