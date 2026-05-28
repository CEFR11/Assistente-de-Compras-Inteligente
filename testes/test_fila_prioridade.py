from estruturas.fila_prioridade import FilaPrioridade

fp = FilaPrioridade()

print("=== Testando inserir e extrair ===")
fp.inserir({'busca': 'celular'}, prioridade =3)
fp.inserir({'busca': 'celular barato com câmera'}, prioridade =6)
fp.inserir({'busca': 'notebook'}, prioridade =3)

print(fp.extrair_max())  # espera: celular barato com câmera (score 6)
print(fp.extrair_max())  # espera: celular (chegou primeiro no empate de score 3)
print(fp.extrair_max())  # espera: notebook

print("\n=== Testando calcular_prioridade ===")
dados1 = {'categoria': 'celular', 'preco': None, 'atributos': []}
dados2 = {'categoria': 'celular', 'preco': 'baixo', 'atributos': ['câmera', 'bateria']}
dados3 = {'categoria': None, 'preco': None, 'atributos': []}

print(f"Só categoria:           score = {fp.calcular_prioridade(dados1)}")  # espera 3
print(f"Categoria+preço+2 atr.: score = {fp.calcular_prioridade(dados2)}")  # espera 7
print(f"Busca vazia:            score = {fp.calcular_prioridade(dados3)}")  # espera 0

print("\n=== Testando fila vazia ===")
try:
    fp.extrair_max()
    print("ERRO: deveria ter dado IndexError!")
except IndexError as e:
    print(f"Correto! Erro capturado: {e}")