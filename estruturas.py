# estruturas/fila_simples.py

class FilaSimples:
    def __init__(self):
        self._fila = []

    def enqueue(self, requisicao: str):
        self._fila.append(requisicao)

    def dequeue(self) -> str:
        if self.esta_vazia():
            raise IndexError("Fila vazia")
        return self._fila.pop(0)

    def esta_vazia(self) -> bool:
        return len(self._fila) == 0

    def tamanho(self) -> int:
        return len(self._fila)