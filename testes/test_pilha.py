from estruturas.pilha import Pilha

pilha = Pilha(capacidade=10)

print("=== Testando push() ===")
pilha.push({"original": "celular barato com boa câmera",
            "categoria": "celular",  "preco": "baixo", "atributos": ["câmera"]})
pilha.push({"original": "fone bluetooth",
            "categoria": "fone",     "preco": None,    "atributos": []})
pilha.push({"original": "notebook gamer até 4000 reais",
            "categoria": "notebook", "preco": "medio", "atributos": []})

print(pilha)

print("\n=== Testando peek() ===")
print(pilha.peek()["original"])

print("\n=== Testando peek() em pilha vazia ===")
print(Pilha().peek())

print("\n=== Testando historico(2) ===")
for h in pilha.historico(2):
    print(h["original"])

print("\n=== Testando categorias_recentes() ===")
print(pilha.categorias_recentes())

print("\n=== Testando pop() ===")
removida = pilha.pop()
print(removida["original"])
print(pilha.peek()["original"])

print("\n=== Testando pop() em pilha vazia ===")
try:
    Pilha().pop()
    print("ERRO: deveria ter dado IndexError!")
except IndexError as e:
    print(f"Correto! Erro capturado: {e}")

print("\n=== Testando capacidade máxima (cap=3) ===")
p3 = Pilha(capacidade=3)
for i in range(4):
    p3.push({"original": f"busca {i}", "categoria": None, "preco": None, "atributos": []})
    print(f"push 'busca {i}' → tamanho={p3.tamanho()}")
print([h["original"] for h in p3.historico(3)])

print("\n=== Testando repr() ===")
print(repr(pilha))