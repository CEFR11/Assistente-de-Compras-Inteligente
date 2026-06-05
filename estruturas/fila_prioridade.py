import heapq

class FilaPrioridade:
    """Eduardo – Fila de prioridade para ordenar buscas por relevância."""

    def __init__(self):
        self._heap = []
        self._counter = 0

    def inserir(self, item: dict, prioridade: int):
        """Prioridade maior = processado primeiro. Usa negativo pois heapq é min-heap."""
        heapq.heappush(self._heap, (-prioridade, self._counter, item))
        self._counter += 1

    def extrair_max(self) -> dict:
        """Remove e retorna o item de maior prioridade. Lança IndexError se vazia."""
        if self.esta_vazia():
            raise IndexError('Fila de prioridade vazia')
        _, _, item = heapq.heappop(self._heap)
        return item

    def esta_vazia(self) -> bool:
        return len(self._heap) == 0

    def calcular_prioridade(self, dados: dict) -> int:
        """
        +3 se tem categoria
        +2 se tem faixa de preço
        +1 por cada atributo
        """
        score = 0
        if dados.get('categoria'): score += 3
        if dados.get('preco'):     score += 2
        if dados.get('atributos'): score += len(dados['atributos'])
        return score