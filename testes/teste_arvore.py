from estruturas.arvore import ArvoreCategorias

arvore = ArvoreCategorias()
arvore.inserir(['Eletrônicos', 'Celulares'], {'id': 'cel001', 'nome': 'Smartphone X', 'preco': 'baixo'})
arvore.inserir(['Eletrônicos', 'Celulares'], {'id': 'cel002', 'nome': 'iPhone 15', 'preco': 'alto'})
arvore.inserir(['Eletrônicos', 'Notebooks'], {'id': 'nb001', 'nome': 'Notebook Pro', 'preco': 'medio'})

resultado = arvore.buscar_categoria(['Eletrônicos', 'Celulares'])
assert len(resultado) == 2
print("Teste 1 passou: busca por subcategoria OK")

resultado = arvore.buscar_categoria(['Eletrônicos'])
assert len(resultado) == 3
print("Teste 2 passou: busca por ramo completo OK")

resultado = arvore.buscar_categoria(['Eletrodomésticos'])
assert resultado == []
print("Teste 3 passou: categoria inexistente retorna [] OK")

arvore.inserir(['Games'], {'id': 'game001', 'nome': 'PlayStation 5', 'preco': 'alto'})
resultado = arvore.buscar_categoria(['Games'])
assert len(resultado) == 1
print("Teste 4 passou: inserção e busca em categoria nova OK")

resultado = arvore.buscar_categoria(['Eletrônicos', 'Celulares'], filtros={'preco': 'baixo'})
assert resultado == [{'id': 'cel001', 'nome': 'Smartphone X', 'preco': 'baixo'}]
print("Teste 5 passou: refinamento por preco OK")

resultado = arvore.buscar_categoria(['Eletrônicos'], filtros={'preco': 'alto'})
assert len(resultado) == 1
print("Teste 6 passou: refinamento por preco no ramo completo OK")

assert arvore.categoria_existe(['Eletrônicos', 'Celulares']) == True
assert arvore.categoria_existe(['Eletrônicos', 'Drones']) == False
print("Teste 7 passou: verificacao de categoria existe OK")

print("\nTodos os testes passaram!")