from estruturas.grafo import GrafoProdutos

grafo = GrafoProdutos()
grafo.adicionar_produto('cel001')
grafo.adicionar_produto('cel002')
grafo.adicionar_produto('nb001')
grafo.adicionar_produto('fone001')

grafo.adicionar_relacao('cel001', 'fone001', 0.9)
grafo.adicionar_relacao('cel001', 'cel002', 0.7)
grafo.adicionar_relacao('nb001', 'fone001', 0.8)
grafo.adicionar_relacao('nb001', 'cel001', 0.5)

resultado = grafo.recomendar('cel001')
assert 'fone001' in resultado
print("Teste 1 passou: recomendacao retorna produtos relacionados OK")

resultado = grafo.recomendar('cel001', top_n=1)
assert resultado == ['fone001']
print("Teste 2 passou: recomendacao respeita top_n OK")

resultado = grafo.recomendar('produto_inexistente')
assert resultado == []
print("Teste 3 passou: produto inexistente retorna [] OK")

assert grafo.grau('cel001') == 3
print("Teste 4 passou: grau do no OK")

assert grafo.produto_existe('nb001') == True
assert grafo.produto_existe('tv001') == False
print("Teste 5 passou: verificacao de produto existe OK")

relacoes = grafo.listar_relacoes()
assert len(relacoes) == 4
print("Teste 6 passou: listagem de relacoes OK")

historico = ['cel001', 'nb001']
resultado = grafo.recomendar_por_historico(historico)
assert 'fone001' in resultado
assert 'cel001' not in resultado
assert 'nb001' not in resultado
print("Teste 7 passou: recomendacao por historico OK")

print("\nTodos os testes passaram!")