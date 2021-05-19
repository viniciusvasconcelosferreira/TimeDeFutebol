from controller import Controller

times = []

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
        nome = input('Entre com o nome do time: ')
        estado = input('Entre com o estado ao qual o time pertence: ')
        titulos = int(input('Entre com a quantidade de titulos que o time possui: '))
        folha_de_pagamento = float(input('Entre com o valor da folha de pagamento do time: '))
        times.append(Controller.inserir(nome, estado, titulos, folha_de_pagamento))
    elif opcao == 2:
        Controller.listar(times)
    elif opcao == 3:
        nome = input('Digite o nome do time para a pesquisa: ')
        Controller.pesquisaNome(times, nome)
    elif opcao == 4:
        print(f"Existem {'0' if len(times) == 0 else len(times)} times cadastrados no sistema")
    elif opcao == 5:
        pass
    elif opcao == 6:
        nome = input('Digite o nome do time para exclusão: ')
        print(Controller.deleteNome(times, nome))
    elif opcao == 7:
        print(Controller.deleteAll(times))
    else:
        print('Obrigado e volte sempre!')
        break
