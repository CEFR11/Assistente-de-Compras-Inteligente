class _No:
    def __init__(self, valor):
        self.valor    = valor
        self.anterior = None
        self.proximo  = None


class Pilha:
    def __init__(self, capacidade: int = 50):
        self._topo       = None
        self._base       = None
        self._tamanho    = 0
        self._capacidade = capacidade

    def push(self, item):
        no = _No(item)
        if self._topo is None:
            self._topo = self._base = no
        else:
            no.anterior        = self._topo
            self._topo.proximo = no
            self._topo         = no
        self._tamanho += 1
        if self._tamanho > self._capacidade:
            self._remover_base()

    def _remover_base(self):
        if self._base is None:
            return
        self._base = self._base.proximo
        if self._base is not None:
            self._base.anterior = None
        else:
            self._topo = None
        self._tamanho -= 1

    def pop(self):
        if self.esta_vazia():
            raise IndexError('Pilha vazia')
        valor      = self._topo.valor
        self._topo = self._topo.anterior
        if self._topo is not None:
            self._topo.proximo = None
        else:
            self._base = None
        self._tamanho -= 1
        return valor

    def voltar(self):
        if self._tamanho < 2:
            return None
        self.pop()
        return self._topo.valor if self._topo else None

    def peek(self):
        return None if self.esta_vazia() else self._topo.valor

    def esta_vazia(self) -> bool:
        return self._topo is None

    def tamanho(self) -> int:
        return self._tamanho

    def historico(self, n: int = 5) -> list:
        items = []
        atual = self._topo
        while atual and len(items) < n:
            items.append(atual.valor)
            atual = atual.anterior
        return items[::-1]

    def categorias_recentes(self, n: int = 5) -> list:
        return [h.get('categoria') for h in self.historico(n) if h.get('categoria')]

    def __repr__(self):
        return f'Pilha({self.historico()})'
