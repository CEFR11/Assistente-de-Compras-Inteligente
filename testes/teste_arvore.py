from estruturas.arvore import ArvoreCategorias

arvore = ArvoreCategorias()
arvore.inserir(['Eletrônicos', 'Celulares'], {'id': 'cel001', 'nome': 'Smartphone X'})
arvore.inserir(['Eletrônicos', 'Celulares'], {'id': 'cel002', 'nome': 'iPhone 15'})
arvore.inserir(['Eletrônicos', 'Notebooks'], {'id': 'nb001', 'nome': 'Notebook Pro'})

resultado = arvore.buscar_categoria(['Eletrônicos', 'Celulares'])
assert resultado == [{'id': 'cel001', 'nome': 'Smartphone X'}, {'id': 'cel002', 'nome': 'iPhone 15'}]
print("Teste 1 passou: busca por subcategoria OK")

resultado = arvore.buscar_categoria(['Eletrônicos'])
assert len(resultado) == 3
print("Teste 2 passou: busca por ramo completo OK")

resultado = arvore.buscar_categoria(['Eletrodomésticos'])
assert resultado == []
print("Teste 3 passou: categoria inexistente retorna [] OK")

arvore.inserir(['Games'], {'id': 'game001', 'nome': 'PlayStation 5'})
resultado = arvore.buscar_categoria(['Games'])
assert resultado == [{'id': 'game001', 'nome': 'PlayStation 5'}]
print("Teste 4 passou: inserção e busca em categoria nova OK")

print("\nTodos os testes passaram!")