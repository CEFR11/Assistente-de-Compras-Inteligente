class GrafoProdutos:
    """Marcos – Grafo não-dirigido de relações entre produtos."""

    def __init__(self):
        self._adj = {}

    def adicionar_produto(self, produto_id: str):
        if produto_id not in self._adj:
            self._adj[produto_id] = {}

    def adicionar_relacao(self, id_a: str, id_b: str, peso: float = 1.0):
        """Insere relação nos dois sentidos. peso = força da co-compra (0.0 a 1.0)."""
        self.adicionar_produto(id_a)
        self.adicionar_produto(id_b)
        self._adj[id_a][id_b] = peso
        self._adj[id_b][id_a] = peso

    def recomendar(self, produto_id: str, top_n: int = 3) -> list:
        """Retorna os top_n produtos mais relacionados por peso."""
        if produto_id not in self._adj:
            return []
        vizinhos = self._adj[produto_id]
        ordenados = sorted(vizinhos, key=lambda x: vizinhos[x], reverse=True)
        return ordenados[:top_n]

    def grau(self, produto_id: str) -> int:
        return len(self._adj.get(produto_id, {}))