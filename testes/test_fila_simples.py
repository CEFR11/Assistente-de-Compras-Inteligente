

from estruturas import FilaSimples

def test_enqueue_dequeue():
    fila = FilaSimples()
    fila.enqueue("celular barato")
    fila.enqueue("notebook")
    assert fila.dequeue() == "celular barato"  # primeiro que entrou
    assert fila.dequeue() == "notebook"

def test_tamanho():
    fila = FilaSimples()
    fila.enqueue("tv grande")
    fila.enqueue("fone premium")
    assert fila.tamanho() == 2

def test_fila_vazia():
    fila = FilaSimples()
    assert fila.esta_vazia() == True

def test_erro_fila_vazia():
    fila = FilaSimples()
    try:
        fila.dequeue()
        assert False  # não devia chegar aqui
    except IndexError:
        assert True  # esperado