class TimeDeFutebol:
    def __init__(self, nm_time, nm_estado, qtd_titulos, vl_folha):
        self._nome = nm_time,
        self._estado = nm_estado,
        self._titulos = qtd_titulos
        self._folhaPagamento = vl_folha

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def titulos(self):
        return self._titulos

    @titulos.setter
    def titulos(self, value):
        self._titulos = value

    @property
    def folhaPagamento(self):
        return self._folhaPagamento

    @folhaPagamento.setter
    def folhaPagamento(self, value):
        self._folhaPagamento = value
