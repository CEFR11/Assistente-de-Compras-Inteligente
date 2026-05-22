class HashTable:
    def __init__(self, capacidade: int = 10):
        self._capacidade = capacidade
        self._tabela = [[] for _ in range(capacidade)]

    def _hash(self, chave: str) -> int:
        return sum(ord(c) for c in chave) % self._capacidade

    def inserir(self, chave: str, valor):
        indice = self._hash(chave)
        bucket = self._tabela[indice]
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)  # atualiza se já existe
                return
        bucket.append((chave, valor))

    def buscar(self, chave: str):
        indice = self._hash(chave)
        for k, v in self._tabela[indice]:
            if k == chave:
                return v
        raise KeyError(f"Chave '{chave}' não encontrada")

    def remover(self, chave: str):
        indice = self._hash(chave)
        bucket = self._tabela[indice]
        for i, (k, v) in enumerate(bucket):
            if k == chave:
                bucket.pop(i)
                return
        raise KeyError(f"Chave '{chave}' não encontrada")

    def contem(self, chave: str) -> bool:
        try:
            self.buscar(chave)
            return True
        except KeyError:
            return False

    def tamanho(self) -> int:
        return sum(len(bucket) for bucket in self._tabela)
    
    def listar_chaves(self) -> list:
        chaves = []
        for bucket in self._tabela:
         for k, v in bucket:
            chaves.append(k)
        return chaves