from collections import deque

class Pilha:

    def __init__(self, capacidade: int = 50):
        self._dados = deque(maxlen=capacidade)

    def push(self, item):
        self._dados.append(item)

    def pop(self):
        if self.esta_vazia():
            raise IndexError('Pilha vazia')
        return self._dados.pop()

    def voltar(self):
        if len(self._dados) < 2:
            return None
        self._dados.pop()
        return self._dados[-1]

    def peek(self):
        if self.esta_vazia():
            return None
        return self._dados[-1]

    def esta_vazia(self) -> bool:
        return len(self._dados) == 0

    def tamanho(self) -> int:
        return len(self._dados)

    def historico(self, n: int = 5) -> list:
        return list(self._dados)[-n:]

    def categorias_recentes(self, n: int = 5) -> list:
        return [h.get('categoria') for h in list(self._dados)[-n:] if h.get('categoria')]

    def __repr__(self):
        return f'Pilha({list(self._dados)})'
