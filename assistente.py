import json
import pathlib
from estruturas.fila_simples    import FilaSimples
from estruturas.fila_prioridade import FilaPrioridade
from estruturas.pilha           import Pilha
from estruturas.hash_table      import HashTable
from estruturas.arvore          import ArvoreCategorias
from estruturas.grafo           import GrafoProdutos
from nucleo.nlp_parser          import NLPParser


class AssistenteDeCompras:

    def __init__(self):
        self.fila_entrada    = FilaSimples()
        self.fila_prioridade = FilaPrioridade()
        self.historico       = Pilha()
        self.catalogo        = HashTable()
        self.arvore          = ArvoreCategorias()
        self.grafo           = GrafoProdutos()
        self.nlp             = NLPParser()
        self._popular_catalogo()

    def buscar(self, texto_usuario: str) -> dict:
        self.fila_entrada.enqueue(texto_usuario)

        req_bruta = self.fila_entrada.dequeue()
        dados = self.nlp.parsear(req_bruta)

        prio = self.fila_prioridade.calcular_prioridade(dados)
        self.fila_prioridade.inserir(dados, prio)

        req       = self.fila_prioridade.extrair_max()
        categoria = req.get('categoria', '')
        faixa     = req.get('preco', '')

        if categoria:
            por_categoria = self.arvore.buscar_categoria(['eletronico', categoria])
            if faixa:
                por_categoria = [p for p in por_categoria if p.get('preco') == faixa]
        elif faixa:
            por_categoria = self.catalogo.buscar_por_atributo('preco', faixa)
        else:
            por_categoria = self.catalogo.listar_todos()

        ids_encontrados = [p['id'] for p in por_categoria]
        recomendacoes = []

        if por_categoria:
            ids_grafo = self.grafo.recomendar(por_categoria[0]['id'])
            recomendacoes = [
                self.catalogo.buscar(pid)
                for pid in ids_grafo
                if self.catalogo.buscar(pid) and pid not in ids_encontrados
            ]

        ids_ja_sugeridos = ids_encontrados + [r['id'] for r in recomendacoes]
        recomendacoes += self._recomendar_por_historico(ids_ja_sugeridos)

        self.historico.push(req)

        return {
            'por_categoria': por_categoria,
            'recomendacoes': recomendacoes,
            'historico':     self.historico.historico(),
        }

    def voltar(self):
        req_anterior = self.historico.voltar()
        if req_anterior is None:
            print('  Nenhuma busca anterior disponível.')
            return None
        texto = req_anterior.get('original', '')
        if not texto:
            return None
        return self.buscar(texto)

    def _recomendar_por_historico(self, excluir_ids: list) -> list:
        hist = self.historico.historico(n=5)
        categorias = [h.get('categoria') for h in hist if h.get('categoria')]
        if not categorias:
            return []
        mais_buscada = max(set(categorias), key=categorias.count)
        candidatos = self.arvore.buscar_categoria(['eletronico', mais_buscada])
        return [p for p in candidatos if p['id'] not in excluir_ids][:2]

    def _popular_catalogo(self):
        produtos = [
            {'id': 'cel001',  'nome': 'Moto G54',           'categoria': 'celular',  'preco': 'baixo', 'valor': 899.00},
            {'id': 'cel002',  'nome': 'Samsung Galaxy A35',  'categoria': 'celular',  'preco': 'medio', 'valor': 1699.00},
            {'id': 'cel003',  'nome': 'iPhone 15',           'categoria': 'celular',  'preco': 'alto',  'valor': 5999.00},
            {'id': 'cel004',  'nome': 'Xiaomi Redmi 13C',    'categoria': 'celular',  'preco': 'baixo', 'valor': 699.00},
            {'id': 'nb001',   'nome': 'Acer Aspire 3',       'categoria': 'notebook', 'preco': 'baixo', 'valor': 2199.00},
            {'id': 'nb002',   'nome': 'Dell Inspiron 15',    'categoria': 'notebook', 'preco': 'medio', 'valor': 3499.00},
            {'id': 'nb003',   'nome': 'MacBook Air M2',      'categoria': 'notebook', 'preco': 'alto',  'valor': 9999.00},
            {'id': 'tv001',   'nome': 'TV TCL 43" 4K',       'categoria': 'tv',       'preco': 'baixo', 'valor': 1299.00},
            {'id': 'tv002',   'nome': 'Samsung 55" QLED',    'categoria': 'tv',       'preco': 'alto',  'valor': 4799.00},
            {'id': 'fone001', 'nome': 'JBL Tune 510BT',      'categoria': 'fone',     'preco': 'baixo', 'valor': 249.00},
            {'id': 'fone002', 'nome': 'Sony WH-1000XM5',     'categoria': 'fone',     'preco': 'alto',  'valor': 2199.00},
        ]

        relacoes = [
            ('cel001',  'cel002',  0.8),
            ('cel002',  'cel003',  0.6),
            ('cel003',  'nb003',   0.7),
            ('nb001',   'nb002',   0.5),
            ('fone001', 'cel001',  0.9),
            ('fone002', 'cel003',  0.85),
            ('tv001',   'tv002',   0.4),
        ]

        for p in produtos:
            self.catalogo.inserir(p['id'], p)
            self.arvore.inserir(['eletronico', p['categoria']], p)
            self.grafo.adicionar_produto(p['id'])

        for a, b, w in relacoes:
            self.grafo.adicionar_relacao(a, b, w)

        grafo_js = {}
        for a, b, w in relacoes:
            grafo_js.setdefault(a, {})[b] = w
            grafo_js.setdefault(b, {})[a] = w

        js = (
            f"const CATALOGO = {json.dumps(produtos, ensure_ascii=False)};\n"
            f"const GRAFO    = {json.dumps(grafo_js,  ensure_ascii=False)};\n"
        )
        pathlib.Path(__file__).parent.joinpath('data.js').write_text(js, encoding='utf-8')


if __name__ == '__main__':
    a = AssistenteDeCompras()

    frases = [
        'celular barato com boa câmera',
        'notebook para trabalho',
        'fone premium',
        'tv grande barata',
        'smartphone topo de linha',
    ]

    for frase in frases:
        print(f'\n🔍 "{frase}"')
        r = a.buscar(frase)
        if r['por_categoria']:
            for p in r['por_categoria']:
                print(f"  • {p['nome']:<25} R$ {p['valor']:>8.2f}  [{p['preco']}]")
        else:
            print('  Nenhum produto encontrado.')
        if r['recomendacoes']:
            print('  Recomendados:')
            for p in r['recomendacoes']:
                print(f"    ↳ {p['nome']}")

    print('\n↩️  Voltando para busca anterior...')
    r = a.voltar()
    if r and r['por_categoria']:
        for p in r['por_categoria']:
            print(f"  • {p['nome']:<25} R$ {p['valor']:>8.2f}  [{p['preco']}]")