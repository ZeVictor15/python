def Quantidade(cod):
    if len(cod) != 13:
        return False
    else:
        return True
def Soma(cod):
    soma1 = 0
    soma2 = 0
    for i in range(0,12,2):
            soma1 += int(cod[i]) * 1
            soma2 += int(cod[i+1]) * 3
    return soma1+soma2
opcao = 0
while opcao != 3: 
    print("--------------------------------------------------")
    print("                   VAREJO S/A")
    print("            (CÓDIGO GTIN-13/UPC/EAN-13) ")
    print("--------------------------------------------------")
    print("         1) Válidar código GTIN-13")
    print("         2) Identificar País ")
    print("         3) Sair")
    print("--------------------------------------------------")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        print("VÁLIDAR CÓDIGO")
        cod1 = str(input("Digite o código de 13 digitos : ")).replace(".","").replace("-","")
        somat = Soma(cod1)//10
        somat += 1
        somat *= 10 
        somat -= (Soma(cod1))
        if somat >= 10:
            somat = 0
        if Quantidade(cod1) == False:
            print("Número de GTIN-13 não possui 13 digitos! ")
            print("--------------------------------------------------")
            (input("Pressione ENTER para continuar..."))            
        else:
            if somat == int(cod1[12]):
                print("Dígito VERIFICADOR: {}".format(somat))
                print("NÚMERO GTIN-13 VÁLIDO")
                input("Pressione ENTER para continuar...")
            elif somat != int(cod1[12]):
                print("Dígito VERIFICADOR:{}".format(somat))
                print("NÚMERO GTIN-13 INVÁLIDO")
                print("--------------------------------------------------")
                input("Pressione ENTER para continuar...")
    elif opcao == 2:
        print("IDENTIFICAR PAÍS")   
        cod1 = str(input("Digite o código de 13 digitos : ")).replace(".","").replace("-","")
        local = int(cod1[0:3])
        if local == 789 or local == 789: 
            print("GTIN-13 de Origem BRASIL: {}".format(local))
            input("Pressione ENTER para continuar...")
        elif local == 779:
            print("GTIN-13 de Origem ARGENTINA : {}".format(local))
            input("Pressione ENTER para continuar...")
        elif local == 773:
            print("GTIN-13 de Origem URUGUAI : {}".format(local))
            input("Pressione ENTER para continuar...")
        elif local == 780:
            print("GTIN-13 de Origem CHILE : {}".format(local))
            input("Pressione ENTER para continuar...")
        elif local == 784:
            print("GTIN-13 de Origem PARAGUAI : {}".format(local))
            input("Pressione ENTER para continuar...")  
        elif local == 786:
            print("GTIN-13 de Origem EQUADOR : {}".format(local))
            input("Pressione ENTER para continuar...")
        elif local == 770:
            print("GTIN-13 de Origem COLÔMBIA : {}".format(local))
            input("Pressione ENTER para continuar...")
        elif local == 743:
            print("GTIN-13 de Origem NICARÁGUA : {}".format(local))
            input("Pressione ENTER para continuar...")
        elif local == 600 or local == 6001:
            print("GTIN-13 de Origem ÁFRICA DO SUL : {}".format(local))
            input("Pressione ENTER para continuar...")
        else:
            print("VAREJOS S/A não vende para este país: {}".format(local))
            input('Pressione ENTER para continuar...') 
    elif opcao == 3:
        break
    else:
        print("Opção INCORRETA!")





            
        