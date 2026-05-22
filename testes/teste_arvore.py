from estruturas.arvore import ArvoreCategorias

arvore = ArvoreCategorias()
arvore.inserir(['Eletrônicos', 'Celulares'], {'id': 'cel001', 'nome': 'Smartphone X'})
arvore.inserir(['Eletrônicos', 'Celulares'], {'id': 'cel002', 'nome': 'iPhone 15'})
arvore.inserir(['Eletrônicos', 'Notebooks'], {'id': 'nb001', 'nome': 'Notebook Pro'})

print(arvore.buscar_categoria(['Eletrônicos', 'Celulares']))
print(arvore.buscar_categoria(['Eletrônicos']))