from estruturas.fila_simples import FilaSimples

def test_enqueue_dequeue():
    f = FilaSimples()
    f.enqueue('celular')
    f.enqueue('notebook')
    assert f.dequeue() == 'celular'
    assert f.dequeue() == 'notebook'

def test_ordem_fifo():
    f = FilaSimples()
    for i in range(5):
        f.enqueue(f'item{i}')
    for i in range(5):
        assert f.dequeue() == f'item{i}'

def test_esta_vazia():
    f = FilaSimples()
    assert f.esta_vazia()
    f.enqueue('x')
    assert not f.esta_vazia()
    f.dequeue()
    assert f.esta_vazia()

def test_tamanho():
    f = FilaSimples()
    assert f.tamanho() == 0
    f.enqueue('a')
    f.enqueue('b')
    assert f.tamanho() == 2
    f.dequeue()
    assert f.tamanho() == 1

def test_dequeue_vazia():
    f = FilaSimples()
    try:
        f.dequeue()
        print('ERRO: deveria ter dado IndexError!')
    except IndexError as e:
        print(f'Correto! Erro capturado: {e}')

def test_repr():
    f = FilaSimples()
    f.enqueue('a')
    assert 'a' in repr(f)

if __name__ == '__main__':
    test_enqueue_dequeue()
    print('test_enqueue_dequeue OK')
    test_ordem_fifo()
    print('test_ordem_fifo OK')
    test_esta_vazia()
    print('test_esta_vazia OK')
    test_tamanho()
    print('test_tamanho OK')
    test_dequeue_vazia()
    test_repr()
    print('test_repr OK')
    print('\nTodos os testes passaram!')
