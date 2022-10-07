from PilhaTAD import Pilha

def padraoXY(string):
    if(len(string) % 2 != 0):
        return False
    else:
        string1 = string [:len(string) // 2]
        string2 = string [len(string) // 2:]
        pilha = Pilha()

        for letra in string1:
            pilha.insere(letra)
        
        for letra in string2:
            if letra != pilha.remove():
                return False
        
        return True

padraoXY('victor')