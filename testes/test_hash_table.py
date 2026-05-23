from estruturas.hash_table import HashTable

def test_inserir_buscar():
    ht = HashTable()
    ht.inserir("celular", {"nome": "Moto G", "preco": 800})
    resultado = ht.buscar("celular")
    assert resultado["nome"] == "Moto G"

def test_atualizar():
    ht = HashTable()
    ht.inserir("celular", {"nome": "Moto G", "preco": 800})
    ht.inserir("celular", {"nome": "Moto G", "preco": 750})
    assert ht.buscar("celular")["preco"] == 750

def test_remover():
    ht = HashTable()
    ht.inserir("notebook", {"nome": "Dell", "preco": 3000})
    ht.remover("notebook")
    assert ht.buscar("notebook") is None  # agora retorna None

def test_contem():
    ht = HashTable()
    ht.inserir("fone", {"nome": "JBL", "preco": 200})
    assert ht.buscar("fone") is not None
    assert ht.buscar("tv") is None

def test_tamanho():
    ht = HashTable()
    ht.inserir("celular", {})
    ht.inserir("notebook", {})
    assert len(ht.listar_todos()) == 2

def test_buscar_inexistente():
    ht = HashTable()
    assert ht.buscar("inexistente") is None  # retorna None em vez de KeyError

def test_remover_inexistente():
    ht = HashTable()
    ht.remover("inexistente")  # não deve lançar erro

def test_listar_todos():
    ht = HashTable()
    ht.inserir("celular", {"nome": "Moto G"})
    ht.inserir("notebook", {"nome": "Dell"})
    todos = ht.listar_todos()
    assert {"nome": "Moto G"} in todos
    assert {"nome": "Dell"} in todos

def test_listar_chaves():
    ht = HashTable()
    ht.inserir("celular", {})
    ht.inserir("notebook", {})
    chaves = ht.listar_chaves()
    assert "celular" in chaves
    assert "notebook" in chaves

def test_repr():
    ht = HashTable()
    ht.inserir("celular", {"nome": "Moto G"})
    resultado = repr(ht)
    assert "celular" in resultado

def test_listar_itens():
    ht = HashTable()
    ht.inserir("celular", {"nome": "Moto G"})
    ht.inserir("notebook", {"nome": "Dell"})
    itens = ht.listar_itens()
    assert ("celular", {"nome": "Moto G"}) in itens
    assert ("notebook", {"nome": "Dell"}) in itens