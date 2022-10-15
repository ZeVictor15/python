from galeria import Galeria
from obras import *
from artista import Artistas
lisGale = []
while True:
    print('-'*44)
    opcao = int(input('1- Adicionar uma unidade a rede de galerias\n2- Realizar ações numa galeria específica\n3- Finalizar Sistema\ndigite a opção: '))
    
    if opcao == 1:
        for i in range(1):
            print('-'*44)
            nome = input('Informe o nome da galeria: ')
            tele = input('Informe o telefone da gelaria: ')
            resp = input('Informe o responsavel pela galeria: ')
            
            add = Galeria(nome,tele,resp)
            lisGale.append(add) 

    elif opcao == 2:
        print('-'*44)
        galeria = input('Digite o nome galeria: ')
        while True:
            print('-'*44)
            for i in lisGale:
                if i.nome != galeria:
                    print('Galeria não cadastrada!!!!')
                else:
                    opcao = str(input('Digite a operação que deseja \n2.1 Cadastrar uma Obra\n2.2 Listar Obras da galeria\n2.3 Listar Obras de um determinado Artista.\n2.4 Avaliar uma obra, a partir do seu código\n2.5 Finalizar atividades nesta galeria\ndigite a opção: '))
                    print('-'*44)
                    if opcao == '2.1':
                        nome = input('Qual o nome do artista: ')
                        naci = input('Qual a nacionalidade do artista: ')
                        data = input('Digite uma data de aquisição: ')
                        titu = input('Digite o titulo: ')
                        tecn = input('Digite a técnica utilizada: ')
                        valo = input('Digite o valor da obra: ')
                        print('-'*44)
                        
                        artista = Artistas(nome,naci)
                        obra = Obra(data,titu,tecn,valo)
                        obra.inserirAutor(artista)
                        
                        i.cadastrarObras(obra)
                
                    elif opcao == '2.2':
                        i.imprimirObras()
                        
            
                    elif opcao == '2.3':
                        nome = input('Digite o nome do autor para pesquisa: ')
                        i.pesquisarObras(nome)
            
                    elif opcao == '2.4':
                        pass
            
                    elif opcao == '2.5':
                        break
            break
        
    elif opcao == 3:
        break