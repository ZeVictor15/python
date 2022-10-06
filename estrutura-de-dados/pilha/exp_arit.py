from PilhaTAD import Pilha

def verifica(entrada):
    pilha=Pilha()
    for c in entrada:
        if  c =='(' or c=='[' or c=='{'  : #se abertura insere na pilha
            pilha.insere(c)
        elif  c ==')' or c==']' or c=='}': # se fechamento
            if(pilha.vazia()):
                return False
            if c== ')' and pilha.remove()!='(': #se fechamento e difere do casal da remocao
                return False
            elif c== ']' and pilha.remove() != '[':
                return False
            elif c== '}' and pilha.remove() != '{':
             return False            
    if pilha.vazia(): #se chegar ao final com a pilha vazia, deu certo
        return True
    else:
        return False           
#string="[(x + y) * 2] = 0"
#string="[(x + y] * 2) = 0"
#string="[(x + y * 2) = 0"
string=list(input("Digite expressão: "))
print(verifica(string))
