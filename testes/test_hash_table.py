from estruturas.hash_table import HashTable

def test_inserir_buscar():
    ht = HashTable()
    ht.inserir("celular", {"nome": "Moto G", "preco": 800})
    resultado = ht.buscar("celular")
    assert resultado["nome"] == "Moto G"

def test_atualizar():
    ht = HashTable()
    ht.inserir("celular", {"nome": "Moto G", "preco": 800})
    ht.inserir("celular", {"nome": "Moto G", "preco": 750})  # atualiza
    assert ht.buscar("celular")["preco"] == 750

def test_remover():
    ht = HashTable()
    ht.inserir("notebook", {"nome": "Dell", "preco": 3000})
    ht.remover("notebook")
    assert ht.contem("notebook") == False

def test_contem():
    ht = HashTable()
    ht.inserir("fone", {"nome": "JBL", "preco": 200})
    assert ht.contem("fone") == True
    assert ht.contem("tv") == False

def test_tamanho():
    ht = HashTable()
    ht.inserir("celular", {})
    ht.inserir("notebook", {})
    assert ht.tamanho() == 2

def test_erro_buscar_inexistente():
    ht = HashTable()
    try:
        ht.buscar("inexistente")
        assert False
    except KeyError:
        assert True

def test_erro_remover_inexistente():
    ht = HashTable()
    try:
        ht.remover("inexistente")
        assert False
    except KeyError:
        assert True
        
def test_listar_chaves():
    ht = HashTable()
    ht.inserir("celular", {})
    ht.inserir("notebook", {})
    chaves = ht.listar_chaves()
    assert "celular" in chaves
    assert "notebook" in chaves