class FilaPrioridade:
    def __init__(self):
        self._heap    = []
        self._counter = 0

    @staticmethod
    def _pai(i):
        return (i - 1) // 2

    @staticmethod
    def _esq(i):
        return 2 * i + 1

    @staticmethod
    def _dir(i):
        return 2 * i + 2

    def _subir(self, i):
        while i > 0:
            pai = self._pai(i)
            if self._heap[i][0] > self._heap[pai][0]:
                self._heap[i], self._heap[pai] = self._heap[pai], self._heap[i]
                i = pai
            else:
                break

    def _descer(self, i):
        n = len(self._heap)
        while True:
            maior = i
            esq   = self._esq(i)
            dir_  = self._dir(i)
            if esq < n and self._heap[esq][0] > self._heap[maior][0]:
                maior = esq
            if dir_ < n and self._heap[dir_][0] > self._heap[maior][0]:
                maior = dir_
            if maior == i:
                break
            self._heap[i], self._heap[maior] = self._heap[maior], self._heap[i]
            i = maior

    def inserir(self, item: dict, prioridade: int):
        self._heap.append((prioridade, self._counter, item))
        self._counter += 1
        self._subir(len(self._heap) - 1)

    def extrair_max(self) -> dict:
        if self.esta_vazia():
            raise IndexError('Fila de prioridade vazia')
        if len(self._heap) == 1:
            return self._heap.pop()[2]
        topo = self._heap[0][2]
        self._heap[0] = self._heap.pop()
        self._descer(0)
        return topo

    def esta_vazia(self) -> bool:
        return len(self._heap) == 0

    def tamanho(self) -> int:
        return len(self._heap)

    def calcular_prioridade(self, dados: dict) -> int:
        score = 0
        if dados.get('categoria'): score += 3
        if dados.get('preco'):     score += 2
        if dados.get('marca'):     score += 2
        if dados.get('atributos'): score += len(dados['atributos'])
        return score

    def __repr__(self):
        return f'FilaPrioridade(tamanho={len(self._heap)})'
