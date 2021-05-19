from team import TimeDeFutebol


class Controller:
    def inserir(nome, estado, titulos, folha_pagamento):
        return TimeDeFutebol(nome, estado, titulos, folha_pagamento)

    def listar(listaTimes):
        print('	NOME 	 | ESTADO | QTD. TITULOS | FOLHA DE PGTO.')
        print('--------------------------------------')
        for time in listaTimes:
            print(
                f'{time.getNome()} 	 | {time.getEstado()}     | {time.getTitulos()}\t\t\t | R$ {time.getFolhaPagamento():.2f}')
            print('--------------------------------------')

    def pesquisaNome(listaTimes, nome):
        contador = 0
        for time in listaTimes:
            if time.getNome() == nome:
                print(f'Nome: {time.getNome()}')
                print(f'Estado: {time.getEstado()}')
                print(f'Qtd. de Titulos: {time.getTitulos()}')
                print(f'Valor da Folha de Pgto.: R$ {time.getFolhaPagamento():.2f}')
                break
            else:
                print(f'Time {nome} não cadastrado no sistema!')
            contador += 1

    def deleteAll(listaTimes):
        if len(listaTimes) != 0:
            listaTimes.clear()
            return 'Todos os times foram removidos!'
        else:
            return 'A lista de times está vazia!'

    def deleteNome(listaTimes, nome):
        if len(listaTimes) != 0:
            cont = 0
            for time in listaTimes:
                if time.getNome() == nome:
                    listaTimes.pop(cont)
                    return f'Time {nome} removido com sucesso!'
                else:
                    return 'Time não encontrado!'
        else:
            return 'Lista de times está vazia!'

    def atualizaFolha(listaTimes, nome, valor):
        if len(listaTimes) != 0:
            for time in listaTimes:
                if time.getNome() == nome:
                    time.setFolhaPagamento(valor)
                    return f'Valor da folha de pagamento do time {nome} atualizado com sucesso!'
                else:
                    return 'Time não encontrado!'
        else:
            return 'Lista de times está vazia!'
