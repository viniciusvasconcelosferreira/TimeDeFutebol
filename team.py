class TimeDeFutebol:
    def __init__(self, nome, estado, titulos, folha_pagamento):
        self.__nome = nome
        self.__estado = estado
        self.__titulos = titulos
        self.__folha_pagamento = folha_pagamento

    def getNome(self):
        return self.__nome

    def setNome(self, value):
        self.__nome = value

    def getEstado(self):
        return self.__estado

    def setEstado(self, value):
        self.__estado = value

    def getTitulos(self):
        return self.__titulos

    def setTitulos(self, value):
        self.__titulos = value

    def getFolhaPagamento(self):
        return self.__folha_pagamento

    def setFolhaPagamento(self, value):
        self.__folha_pagamento = value
