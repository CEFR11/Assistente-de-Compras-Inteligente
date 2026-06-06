class Pilha:

    def init(self, capacidade: int = 50):
        self._dados = []
        self._capacidade = capacidade

    def push(self, item):
        if len(self._dados) >= self._capacidade:
            self._dados.pop(0)
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

    def historico(self, n: int = 5) -> list:
        return self._dados[-n:]