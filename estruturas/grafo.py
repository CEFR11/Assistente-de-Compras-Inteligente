class GrafoProdutos:
    def __init__(self):
        self._adj = {}

    def adicionar_produto(self, produto_id):
        if produto_id not in self._adj:
            self._adj[produto_id] = {}

    def adicionar_relacao(self, id_a, id_b, peso=1.0):
        self.adicionar_produto(id_a)
        self.adicionar_produto(id_b)
        self._adj[id_a][id_b] = peso
        self._adj[id_b][id_a] = peso

    def recomendar(self, produto_id, top_n=3):
        if produto_id not in self._adj:
            return []
        vizinhos = self._adj[produto_id]
        ordenados = sorted(vizinhos, key=lambda x: vizinhos[x], reverse=True)
        return ordenados[:top_n]

    def recomendar_por_historico(self, historico, top_n=3):
        if not historico:
            return []
        pontuacao = {}
        for produto_id in historico:
            if produto_id not in self._adj:
                continue
            for vizinho, peso in self._adj[produto_id].items():
                if vizinho in historico:
                    continue
                if vizinho not in pontuacao:
                    pontuacao[vizinho] = 0
                pontuacao[vizinho] += peso
        ordenados = sorted(pontuacao, key=lambda x: pontuacao[x], reverse=True)
        return ordenados[:top_n]

    def grau(self, produto_id):
        return len(self._adj.get(produto_id, {}))

    def produto_existe(self, produto_id):
        return produto_id in self._adj

    def listar_produtos(self):
        return list(self._adj.keys())

    def listar_relacoes(self):
        relacoes = []
        visitados = set()
        for id_a in self._adj:
            for id_b, peso in self._adj[id_a].items():
                par = tuple(sorted([id_a, id_b]))
                if par not in visitados:
                    relacoes.append((id_a, id_b, peso))
                    visitados.add(par)
        return relacoes