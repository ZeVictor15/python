from agenda import Agenda
from contato import *

while True:
    
    print('-'*40)
    print('1- Inserir Contato: \n2- Pesquisar Contato: \n3- Alterar Contato:  \n4- Sair: ')
    opcao = int(input('Digite a opção: '))
    print('-'*40)
    
    if opcao == 1:
        
        nome = input('Digite o nome do Contato: ')
        email = input('Digite o email do Contato: ')
        ddd = input('Digite o ddd do número: ')
        numero = input('Digite o número: ')
        descricao = input('Digite a descrição do contato: ')
        
        contato = Contato(nome,email)
        contato.add_telefone(ddd,numero,descricao)
        agenda = Agenda()
        agenda.add_contato(contato)
        
    elif opcao == 2:
        nome = input('Digite o nome para a pesquisa: ')
        agenda.pesquisar_nome(nome)
        
    elif opcao == 3:
        while True:
            
            print('3.1- Alterar nome: \n3.2- Alterar E-mail:  \n3.3-Sair: ')
            opcao = str(input('Digite a opção: '))
            
            if opcao == '3.1':
                nome = input('Digite o novo nome: ')
                contato.alterar_nome(nome)
            
            elif opcao == '3.2':
                email = input('Digite o novo email: ')
                contato.alterar_email(email)
            
            elif opcao == '3.3':
                break
            
    elif opcao == 4:
        break