pesoTotal = 0
cont = 0
while True:
    peso = int(input("Você esta na fila do elavador por questão de segurança degite seu peso: "))
    pesoTotal += peso
    cont += 1
    
    if pesoTotal > 800:
        pesoTotal -= peso
        cont -= 1
        print("Peso maximo excedido por favor aguarde o próximo elevador")
        print(f"O peso total é {pesoTotal} e quantidade de pessoas é {cont}")
        break