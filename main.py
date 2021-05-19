from controller import Controller

timesDeFutebol = []

print('|=============================|')
print('|BEM VINDO A LISTAGEM DE TIMES|')
print('|=============================|')
print()
while True:
    print('|=============================|')
    print('|            MENU             |')
    print('|=============================|')
    print('|1 - Adicionar                |')
    print('|2 - Listar                   |')
    print('|3 - Pesquisar                |')
    print('|4 - Qtd. de Cadastros        |')
    print('|5 - Atualizar                |')
    print('|6 - Excluir Time             |')
    print('|7 - Excluir Times            |')
    print('|8 - Sair                     |')
    print('|=============================|')
    opcao = int(input('Escolha uma das opções acima: '))

    if opcao == 1:
        print('|================================|')
        print('|        CADASTRO DE TIME        |')
        print('|================================|')
        nome = input('Entre com o nome do time: ')
        estado = input('Entre com o estado ao qual o time pertence: ')
        titulos = int(input('Entre com a quantidade de titulos que o time possui: '))
        folha_de_pagamento = float(input('Entre com o valor da folha de pagamento do time: '))
        timesDeFutebol.append(Controller.inserir(nome, estado, titulos, folha_de_pagamento))
        print(f'Time {nome} cadastrado com sucesso!')
        print()
    elif opcao == 2:
        print('|=================================|')
        print('|        LISTAGEM DE TIMES        |')
        print('|=================================|')
        Controller.listar(timesDeFutebol)
        print()
    elif opcao == 3:
        print('|================================|')
        print('|        PESQUISA DE TIME        |')
        print('|================================|')
        nome = input('Digite o nome do time para a pesquisa: ')
        Controller.pesquisaNome(timesDeFutebol, nome)
        print()
    elif opcao == 4:
        print('|==================================|')
        print('|            QUANTIDADE            |')
        print('|        DE TIMES CADASTRADOS      |')
        print('|            NO SISTEMA            |')
        print('|==================================|')
        print(f"Existem {'0' if len(timesDeFutebol) == 0 else len(timesDeFutebol)} times cadastrados no sistema")
        print()
    elif opcao == 5:
        print('|================================|')
        print('|   ATUALIZAR CADASTRO DE TIME   |')
        print('|================================|')
        nome = input('Digite o nome do time para a atualização: ')
        valor = float(input('Digite o novo valor da folha de pagamento do time: '))
        print(Controller.atualizaFolha(timesDeFutebol, nome, valor))
        print()
    elif opcao == 6:
        print('|================================|')
        print('|        EXCLUSÃO DE TIME        |')
        print('|================================|')
        nome = input('Digite o nome do time para exclusão: ')
        print(Controller.deleteNome(timesDeFutebol, nome))
    elif opcao == 7:
        print('|================================|')
        print('|    ZERAR REGISTRO DOS TIMES    |')
        print('|================================|')
        print(Controller.deleteAll(timesDeFutebol))
    else:
        print('Obrigado e volte sempre!')
        break
