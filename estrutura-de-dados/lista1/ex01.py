num = []
for i in range(0,5):
    num.append(int(input(f"Digite o elemento de número {i}: ").format()))

maior = max(num)    
menor = min(num)   
print(f"O maior valor é: {maior} é sua posição é {num.index(maior)}".format())
print(f"O menor valor é: {menor} é sua posição é {num.index(menor)}".format())


