class Pilha:

    def __init__(self, capacidade: int = 50):
        self._dados = []
        self._capacidade = capacidade

    def push(self, item: dict) -> None:

        if len(self._dados) >= self._capacidade:
            self._dados.pop(0)          
        self._dados.append(item)

    def pop(self) -> dict:

        if self.esta_vazia():
            raise IndexError("pop() em pilha vazia.")
        return self._dados.pop()

    def peek(self):

        if self.esta_vazia():
            return None
        return self._dados[-1]

    def historico(self, n: int = 5) -> list:

        return self._dados[-n:]

    def esta_vazia(self) -> bool:
        return len(self._dados) == 0

    def tamanho(self) -> int:
        return len(self._dados)

    def categorias_recentes(self) -> list[str]:

        vistas = set()
        resultado = []
        for item in reversed(self._dados):
            cat = item.get("categoria")
            if cat and cat not in vistas:
                vistas.add(cat)
                resultado.append(cat)
        return resultado

    def __repr__(self) -> str:
        if self.esta_vazia():
            return "Pilha(vazia)"
        topo = self._dados[-1].get("original", str(self._dados[-1]))
        return f"Pilha(tamanho={self.tamanho()}, topo='{topo}')"

    def __str__(self) -> str:
        if self.esta_vazia():
            return "[pilha vazia]"
        linhas = ["--- PILHA (topo → base) ---"]
        for i, item in enumerate(reversed(self._dados)):
            prefixo = "► TOPO" if i == 0 else f"  [{self.tamanho() - 1 - i}]"
            texto = item.get("original", str(item))
            linhas.append(f"{prefixo}  {texto}")
        linhas.append("---------------------------")
        return "\n".join(linhas)

if __name__ == "__main__":
    buscas_parsed = [
        {"original": "celular barato com boa câmera",
         "categoria": "celular", "preco": "baixo", "atributos": ["câmera"]},
        {"original": "fone bluetooth",
         "categoria": "fone",    "preco": None,    "atributos": []},
        {"original": "notebook gamer até 4000 reais",
         "categoria": "notebook","preco": "medio", "atributos": []},
    ]

    pilha = Pilha(capacidade=10)

    print("=== SEMANA 1 — Testes unitários da Pilha ===\n")

    print("[ push() ] adicionando buscas:")
    for b in buscas_parsed:
        pilha.push(b)
        print(f"  + '{b['original']}'")

    print(f"\n{pilha}\n")

    print("[ peek() ] última busca (sem remover):")
    print(f"  → '{pilha.peek()['original']}'\n")

    print("[ historico(2) ] últimas 2 buscas:")
    for h in pilha.historico(2):
        print(f"  · {h['original']}")

    print(f"\n[ categorias_recentes() ] → {pilha.categorias_recentes()}")

    print("\n[ pop() ] voltando para busca anterior:")
    removida = pilha.pop()
    print(f"  removido: '{removida['original']}'")
    print(f"  novo topo: '{pilha.peek()['original']}'\n")

    print("[ pop() em pilha vazia ]")
    pilha2 = Pilha()
    try:
        pilha2.pop()
    except IndexError as e:
        print(f"  IndexError capturado: {e}")

    print("\n[ capacidade máxima ] pilha com cap=3:")
    p3 = Pilha(capacidade=3)
    for i in range(4):
        b = {"original": f"busca {i}", "categoria": None, "preco": None, "atributos": []}
        p3.push(b)
        print(f"  push 'busca {i}' → tamanho={p3.tamanho()}")
    print(f"  histórico final: {[h['original'] for h in p3.historico(3)]}")

    print(f"\n{pilha!r}")