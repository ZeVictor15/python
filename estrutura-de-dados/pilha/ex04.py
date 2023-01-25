from PilhaTAD import Pilha

def conversãoPilha(nume,base):
    pilha  = Pilha()
    pilha2 = Pilha()
    
    if base == 2:
        while nume // 2 >= 1:
            pilha.insere(nume % 2)
            nume = nume // 2
            if nume < 2:
                pilha.insere(1)
        for i in range(len(pilha)):
            pilha2.insere(pilha.remove())
        return pilha2
    
    elif base == 8:
        while nume // 8 >= 1:
            pilha.insere(nume % 8)
            nume = nume // 8
        if nume < 8:
            pilha.insere(nume)
        for i in range(len(pilha)):
            pilha2.insere(pilha.remove())
        return pilha2
    
    elif base == 16:
        while nume % 16 >= 1:
            if nume % 16 == 10:
                pilha.insere('A')
            elif nume % 16 == 11:
                pilha.insere('B')
            elif nume % 16 == 12:
                pilha.insere('C')
            elif nume % 16 == 13:
                pilha.insere('D')
            elif nume % 16 == 14:
                pilha.insere('E')
            elif nume % 16 == 15:
                pilha.insere('F')
            nume = nume // 16
            if nume < 16:
                pilha.insere(nume)
                break
        for i in range(len(pilha)):
            pilha2.insere(pilha.remove())
        return pilha2
    else:
        print('Base invalidade. Use Base 2,8 ou 16')

print('O numero em base binaria é:',conversãoPilha(78,2))
print('O numero em base binaria é:',conversãoPilha(78,8))
print('O numero em base binaria é:',conversãoPilha(78,16))