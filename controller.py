from team import TimeDeFutebol


class Controller():
    def inserir(nome, estado, titulos, folhaPagamento):
        return TimeDeFutebol(nome, estado, titulos, folhaPagamento)

    def listar(listaTimes):
        print('NOME | ESTADO | QTD. TITULOS | FOLHA DE PGTO. ')
        print('--------------------------------------')
        for time in listaTimes:
            print(f'{time.nome} | {time.estado} | {time.titulos} | R$ {time.folhaPagamento}')
            print('--------------------------------------')

    def pesquisaNome(listaTimes, nome):
        contador = 0
        for time in listaTimes:
            if time.nome == nome:
                print(f'Nome: {time.nome}')
                print(f'Estado: {time.estado}')
                print(f'Qtd. de Titulos: {time.titulos}')
                print(f'Valor da Folha de Pgto.: {time.folhaPagamento}')
                break
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
            for tel in listaTimes:
                if tel.getNome() == nome:
                    listaTimes.pop(cont)
                    return f'Time {nome} removido com sucesso!'
                else:
                    return 'Time não encontrado!'
        else:
            return 'Lista de times está vazia!'
