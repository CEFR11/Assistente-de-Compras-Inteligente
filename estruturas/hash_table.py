class HashTable:
    """Pedro 2 – Hash table com chaining para busca rápida de produtos."""

    def __init__(self, capacidade: int = 100):
        self._capacidade = capacidade
        self._tabela = [[] for _ in range(capacidade)]

    def _hash(self, chave: str) -> int:
        return hash(chave) % self._capacidade

    def inserir(self, chave: str, produto: dict):
        """Insere ou atualiza produto na tabela."""
        idx = self._hash(chave)
        for i, (k, _) in enumerate(self._tabela[idx]):
            if k == chave:
                self._tabela[idx][i] = (chave, produto)
                return
        self._tabela[idx].append((chave, produto))

    def buscar(self, chave: str):
        """Retorna o produto ou None se não encontrado."""
        idx = self._hash(chave)
        for k, v in self._tabela[idx]:
            if k == chave:
                return v
        return None

    def buscar_por_atributo(self, campo: str, valor) -> list:
        """Retorna todos os produtos onde produto[campo] == valor.
        Exemplo: buscar_por_atributo('preco', 'baixo')"""
        resultado = []
        for bucket in self._tabela:
            for _, produto in bucket:
                if produto.get(campo) == valor:
                    resultado.append(produto)
        return resultado

    def remover(self, chave: str):
        """Remove o produto da tabela."""
        idx = self._hash(chave)
        self._tabela[idx] = [(k, v) for k, v in self._tabela[idx] if k != chave]

    def listar_todos(self) -> list:
        """Retorna todos os produtos cadastrados."""
        return [v for bucket in self._tabela for _, v in bucket]