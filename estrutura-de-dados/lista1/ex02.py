num = []
numero = 0
while True:
    numero = int(input("Digite um número para salvar na lista digite 0 se quiser encerrar o programa: "))
    if numero == 0:
        break
    num.append(numero)
print(f"A lista de números que você digitou é {num}, é o maior número digitado é {max(num)}")