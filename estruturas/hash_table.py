class HashTable:
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

    def buscar_por_atributo(self, campo: str, valor) -> list:
        resultado = []
        for bucket in self._tabela:
            for _, produto in bucket:
                if produto.get(campo) == valor:
                    resultado.append(produto)
        return resultado

    def remover(self, chave: str):
        idx = self._hash(chave)
        self._tabela[idx] = [(k, v) for k, v in self._tabela[idx] if k != chave]

    def listar_todos(self) -> list:
        return [v for bucket in self._tabela for _, v in bucket]

    def listar_chaves(self) -> list:
        return [k for bucket in self._tabela for k, _ in bucket]

    def listar_itens(self) -> list:
        return [(k, v) for bucket in self._tabela for k, v in bucket]

    def __repr__(self):
        return f'HashTable({dict(self.listar_itens())})'
