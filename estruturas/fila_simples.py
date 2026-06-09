class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class FilaSimples:
    def __init__(self):
        self._inicio = None
        self._fim    = None
        self._tamanho = 0

    def enqueue(self, requisicao: str):
        no = _No(requisicao)
        if self._fim is None:
            self._inicio = self._fim = no
        else:
            self._fim.proximo = no
            self._fim = no
        self._tamanho += 1

    def dequeue(self) -> str:
        if self.esta_vazia():
            raise IndexError('Fila vazia')
        valor = self._inicio.valor
        self._inicio = self._inicio.proximo
        if self._inicio is None:
            self._fim = None
        self._tamanho -= 1
        return valor

    def esta_vazia(self) -> bool:
        return self._inicio is None

    def tamanho(self) -> int:
        return self._tamanho

    def __repr__(self):
        items = []
        atual = self._inicio
        while atual:
            items.append(repr(atual.valor))
            atual = atual.proximo
        return f'FilaSimples([{", ".join(items)}])'
