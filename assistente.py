from estruturas.fila_simples    import FilaSimples
from estruturas.fila_prioridade import FilaPrioridade
from estruturas.pilha           import Pilha
from estruturas.hash_table      import HashTable
from estruturas.arvore          import ArvoreCategorias
from estruturas.grafo           import GrafoProdutos
from nucleo.nlp_parser          import NLPParser
from dados.catalogo             import PRODUTOS, RELACOES


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
        marca     = req.get('marca', '')

        if not categoria and not faixa and not marca:
            return {'por_categoria': [], 'recomendacoes': [], 'historico': self.historico.historico()}

        if categoria:
            por_categoria = self.arvore.buscar_categoria(['eletronico', categoria])
            if faixa:
                por_categoria = [p for p in por_categoria if p.get('preco') == faixa]
        elif faixa:
            por_categoria = self.catalogo.buscar_por_atributo('preco', faixa)
        else:
            por_categoria = self.catalogo.listar_todos()

        if marca:
            por_categoria = [p for p in por_categoria if p.get('marca') == marca]

        atributos = req.get('atributos', [])
        if atributos:
            filtrados = [p for p in por_categoria
                         if any(a in p.get('atributos', []) for a in atributos)]
            if filtrados:
                por_categoria = filtrados

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
        recomendacoes += self._recomendar_por_historico(ids_ja_sugeridos, categoria)

        self.historico.push(req)

        return {
            'por_categoria': por_categoria,
            'recomendacoes': recomendacoes,
            'historico':     self.historico.historico(),
        }

    def voltar(self):
        req_anterior = self.historico.voltar()
        if req_anterior is None:
            return None
        texto = req_anterior.get('original', '')
        if not texto:
            return None
        return self.buscar(texto)

    def _recomendar_por_historico(self, excluir_ids: list, categoria_atual: str = '') -> list:
        hist = self.historico.historico(n=5)
        categorias = [h.get('categoria') for h in hist
                      if h.get('categoria') and h.get('categoria') != categoria_atual]
        if not categorias:
            return []
        mais_buscada = max(set(categorias), key=categorias.count)
        candidatos = self.arvore.buscar_categoria(['eletronico', mais_buscada])
        return [p for p in candidatos if p['id'] not in excluir_ids][:2]

    def _popular_catalogo(self):
        for p in PRODUTOS:
            self.catalogo.inserir(p['id'], p)
            self.arvore.inserir(['eletronico', p['categoria']], p)
            self.grafo.adicionar_produto(p['id'])

        for a, b, w in RELACOES:
            self.grafo.adicionar_relacao(a, b, w)
