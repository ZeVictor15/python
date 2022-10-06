import random

print("Boas vindas ao meu programa!!! Será sorteado um número aleatorio de 0 a 10 e você terá 3 tentivas para acertar qual o número")
numSort = random.randint(0,10)
cont = 0
for i in range(0,3):
    cont += 1
    num = int(input("Digite um número entre 0 e 10: "))
  
    while num > 10:
        print("Número invalido")
        num = int(input("Digite um número entre 0 e 10: "))
        if num < 10:
            break
    
    if num < numSort:
        print("O número é maior que o número digito")

    if num > numSort:
        print("O número é menor que o número digito")
    
    if num == numSort:
        print("Você ganhou o jogo parabéns")
        break
    
    if cont == 3:
        print(f"Você perdeu game tente novamente!!!! o número aleatorio era {numSort}" )
    
