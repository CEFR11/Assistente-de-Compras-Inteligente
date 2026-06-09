class GrafoProdutos:

    def __init__(self):
        self._adj = {}

    def adicionar_produto(self, produto_id: str):
        if produto_id not in self._adj:
            self._adj[produto_id] = {}

    def adicionar_relacao(self, id_a: str, id_b: str, peso: float = 1.0):
        self.adicionar_produto(id_a)
        self.adicionar_produto(id_b)
        self._adj[id_a][id_b] = peso
        self._adj[id_b][id_a] = peso

    def recomendar(self, produto_id: str, top_n: int = 3) -> list:
        if produto_id not in self._adj:
            return []
        vizinhos = self._adj[produto_id]
        ordenados = sorted(vizinhos, key=lambda x: vizinhos[x], reverse=True)
        return ordenados[:top_n]

    def recomendar_por_historico(self, historico_ids: list, top_n: int = 5) -> list:
        scores = {}
        for pid in historico_ids:
            for vizinho, peso in self._adj.get(pid, {}).items():
                if vizinho not in historico_ids:
                    scores[vizinho] = scores.get(vizinho, 0) + peso
        ordenados = sorted(scores, key=lambda x: scores[x], reverse=True)
        return ordenados[:top_n]

    def produto_existe(self, produto_id: str) -> bool:
        return produto_id in self._adj

    def listar_relacoes(self) -> list:
        vistas = set()
        relacoes = []
        for id_a, vizinhos in self._adj.items():
            for id_b, peso in vizinhos.items():
                par = tuple(sorted([id_a, id_b]))
                if par not in vistas:
                    vistas.add(par)
                    relacoes.append((id_a, id_b, peso))
        return relacoes

    def grau(self, produto_id: str) -> int:
        return len(self._adj.get(produto_id, {}))
