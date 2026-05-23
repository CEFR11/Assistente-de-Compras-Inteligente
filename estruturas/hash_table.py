class HashTable:
    """Pedro 2 – Hash table para armazenar e buscar produtos rapidamente."""
    def __init__(self, capacidade: int = 100):
        self._capacidade = capacidade
        self._tabela = [[] for _ in range(capacidade)]

    def _hash(self, chave: str) -> int:
        return hash(chave) % self._capacidade

    def inserir(self, chave: str, produto: dict):
        idx = self._hash(chave)
        for i, (k, _) in enumerate(self._tabela[idx]):
            if k == chave:
                self._tabela[idx][i] = (chave, produto)
                return
        self._tabela[idx].append((chave, produto))

    def buscar(self, chave: str):
        idx = self._hash(chave)
        for k, v in self._tabela[idx]:
            if k == chave:
                return v
        return None

    def remover(self, chave: str):
        idx = self._hash(chave)
        self._tabela[idx] = [(k, v) for k, v in self._tabela[idx] if k != chave]

    def listar_todos(self) -> list:
        return [v for bucket in self._tabela for _, v in bucket]

    def listar_chaves(self) -> list:
        chaves = []
        for bucket in self._tabela:
            for k, v in bucket:
                chaves.append(k)
        return chaves

    def listar_itens(self) -> list:
        itens = []
        for bucket in self._tabela:
            for k, v in bucket:
                itens.append((k, v))
        return itens

    def __repr__(self) -> str:
        itens = []
        for bucket in self._tabela:
            for k, v in bucket:
                itens.append(f"{k}: {v}")
        return "{" + ", ".join(itens) + "}"