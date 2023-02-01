def bubblesort(lista):
    while True:
        flag = False
        for i in range(len(lista)):
            if i+1 < len(lista) and lista[i] > lista[i+1]:
                auxiliar = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = auxiliar
                flag = True
        if flag == False:
                break
    return lista

L1= [5,2,9,7]
L2=[("Carlos",70),("João",20),("Cris", 40)]
print(bubblesort(L1))
print(bubblesort(L2))
