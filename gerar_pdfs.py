from fpdf import FPDF
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FR = 'C:/Windows/Fonts/arial.ttf'
FB = 'C:/Windows/Fonts/arialbd.ttf'
FI = 'C:/Windows/Fonts/ariali.ttf'

class Doc(FPDF):
    PURPLE = (108, 99, 255)
    DARK   = (30, 30, 60)
    MUTED  = (110, 110, 160)
    LIGHT  = (240, 240, 255)

    def __init__(self, header_label=''):
        super().__init__()
        self.add_font('F', '',  FR)
        self.add_font('F', 'B', FB)
        self.add_font('F', 'I', FI)
        self.set_auto_page_break(True, margin=22)
        self.set_margins(22, 22, 22)
        self._hlabel = header_label

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font('F', 'I', 8)
        self.set_text_color(*self.MUTED)
        self.cell(0, 6, self._hlabel, align='R')
        self.ln(2)
        self.set_draw_color(*self.PURPLE)
        self.set_line_width(0.3)
        self.line(22, self.get_y(), 188, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-16)
        self.set_draw_color(*self.PURPLE)
        self.set_line_width(0.3)
        self.line(22, self.get_y() - 2, 188, self.get_y() - 2)
        self.set_font('F', '', 8)
        self.set_text_color(*self.MUTED)
        self.cell(0, 8, f'Página {self.page_no()}', align='C')

    def capa(self, titulo, subtitulo):
        self.add_page()
        self.set_fill_color(*self.PURPLE)
        self.rect(0, 0, 210, 80, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font('F', 'B', 24)
        self.set_xy(22, 15)
        self.multi_cell(166, 11, titulo, align='C')
        self.set_font('F', '', 13)
        self.set_xy(22, 58)
        self.cell(166, 8, subtitulo, align='C')
        self.set_text_color(*self.DARK)
        self.set_font('F', '', 10)
        self.set_y(100)
        for l in ['Disciplina: Programação II — 2025',
                  'Projeto: Assistente de Compras Inteligente',
                  'Data: 08/06/2026']:
            self.cell(0, 8, l, align='C', ln=True)
        self.set_fill_color(*self.PURPLE)
        self.rect(0, 268, 210, 30, 'F')

    def h1(self, num, txt):
        self.ln(6)
        self.set_fill_color(*self.PURPLE)
        self.set_text_color(255, 255, 255)
        self.set_font('F', 'B', 12)
        self.cell(0, 9, f'   {num}.  {txt}', fill=True, ln=True)
        self.set_text_color(*self.DARK)
        self.ln(3)

    def h2(self, txt):
        self.ln(4)
        self.set_font('F', 'B', 11)
        self.set_text_color(*self.PURPLE)
        self.cell(0, 7, txt, ln=True)
        self.set_text_color(*self.DARK)

    def p(self, txt):
        self.set_font('F', '', 10)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5.5, txt)
        self.ln(2)

    def li(self, txt, bold=''):
        self.set_x(27)
        self.set_font('F', '', 10)
        self.set_text_color(*self.DARK)
        self.cell(5, 6, '•')
        if bold:
            self.set_font('F', 'B', 10)
            self.set_text_color(*self.PURPLE)
            self.cell(self.get_string_width(bold) + 2, 6, bold)
            self.set_font('F', '', 10)
            self.set_text_color(*self.DARK)
            self.multi_cell(0, 6, txt)
        else:
            self.multi_cell(0, 6, txt)

    def box(self, label, body):
        self.ln(2)
        self.set_fill_color(*self.LIGHT)
        self.set_draw_color(*self.PURPLE)
        self.set_line_width(0.3)
        self.set_font('F', 'B', 9)
        self.set_text_color(*self.PURPLE)
        self.cell(0, 7, f'  {label}', fill=True, border='LTR', ln=True)
        self.set_font('F', '', 9)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 5.5, f'  {body}', border='LBR', fill=True)
        self.ln(2)

    def tabela(self, header, rows, widths):
        self.set_fill_color(*self.PURPLE)
        self.set_text_color(255, 255, 255)
        self.set_font('F', 'B', 9)
        for txt, w in zip(header, widths):
            self.cell(w, 7, f'  {txt}', fill=True, border=1)
        self.ln()
        for i, row in enumerate(rows):
            self.set_fill_color(245, 245, 255) if i % 2 == 0 else self.set_fill_color(255, 255, 255)
            self.set_text_color(*self.DARK)
            self.set_font('F', '', 9)
            for txt, w in zip(row, widths):
                self.cell(w, 6, f'  {txt}', fill=True, border=1)
            self.ln()
        self.ln(3)

    def badge(self, category, text, detail=''):
        self.set_fill_color(*self.LIGHT)
        self.set_font('F', 'B', 8)
        self.set_text_color(*self.PURPLE)
        self.cell(32, 7, f'  {category}', fill=True, border=0)
        self.set_font('F', 'B', 10)
        self.set_text_color(*self.DARK)
        self.multi_cell(0, 7, text)
        if detail:
            self.set_x(54)
            self.set_font('F', 'I', 9)
            self.set_text_color(*self.MUTED)
            self.multi_cell(0, 5, detail)
        self.ln(1)


# ─────────────────────────────────────────────────────────────
#  DOCUMENTO 1 — DOCUMENTAÇÃO TÉCNICA COMPLETA
# ─────────────────────────────────────────────────────────────
def doc_tecnica():
    pdf = Doc('Assistente de Compras Inteligente — Documentação Técnica')
    pdf.capa('Assistente de Compras\nInteligente', 'Documentação Técnica Completa')

    # ── Introdução ───────────────────────────────────────────
    pdf.add_page()
    pdf.h1(1, 'Introdução')
    pdf.p(
        'O Assistente de Compras Inteligente é um sistema desenvolvido na disciplina '
        'de Programação II que interpreta buscas escritas em linguagem natural e retorna '
        'recomendações de produtos de forma organizada e eficiente.'
    )
    pdf.p(
        'A motivação do projeto parte de um problema cotidiano: o usuário muitas vezes '
        'não sabe o nome exato do produto que quer. Ele pesquisa "celular barato com boa '
        'câmera" ou "notebook da Samsung para trabalho". O sistema interpreta essa '
        'intenção e apresenta resultados relevantes.'
    )
    pdf.h2('Objetivos')
    pdf.li('Interpretar buscas em linguagem natural (NLP)')
    pdf.li('Organizar produtos com estruturas de dados eficientes')
    pdf.li('Gerar recomendações inteligentes baseadas em relações e histórico')
    pdf.li('Reconhecer categorias, preços, atributos e marcas de produtos')
    pdf.li('Aplicar na prática as estruturas de dados estudadas na disciplina')

    # ── Arquitetura ──────────────────────────────────────────
    pdf.h1(2, 'Arquitetura e Fluxo de Processamento')
    pdf.p(
        'O sistema processa cada busca em uma sequência de etapas bem definidas, onde '
        'cada estrutura de dados tem uma responsabilidade específica.'
    )
    pdf.box(
        'Fluxo completo de uma busca',
        '1. Usuário digita a busca na interface web\n'
        '2. Fila Simples (FIFO) recebe e ordena as requisições\n'
        '3. NLP Parser interpreta a frase e extrai: categoria, preço, marca, atributos\n'
        '4. Fila de Prioridade ordena a busca por relevância (score)\n'
        '5. Árvore de Categorias localiza os produtos correspondentes\n'
        '6. Hash Table permite acesso direto a qualquer produto por ID\n'
        '7. Grafo de Produtos gera recomendações ("quem comprou X também comprou Y")\n'
        '8. Pilha armazena o histórico e sugere produtos baseados em buscas anteriores\n'
        '9. Resultados são retornados via API JSON para o frontend'
    )

    # ── Estruturas de Dados ──────────────────────────────────
    pdf.h1(3, 'Estruturas de Dados')

    pdf.h2('3.1  Fila Simples — FIFO (First In, First Out)')
    pdf.p('Arquivo: estruturas/fila_simples.py')
    pdf.p(
        'Primeira estrutura a receber as entradas do usuário. Garante que todas as '
        'requisições sejam processadas na ordem exata de chegada, sem perda de dados '
        'em cenários de múltiplas requisições simultâneas.'
    )
    pdf.p('Implementada com collections.deque para operação O(1) nas duas extremidades.')
    pdf.li('enqueue(req): adiciona requisição ao final da fila — O(1)')
    pdf.li('dequeue(): remove e retorna a requisição mais antiga — O(1)')
    pdf.li('esta_vazia(), tamanho(): consultas de estado')

    pdf.h2('3.2  Fila de Prioridade (Max-Heap)')
    pdf.p('Arquivo: estruturas/fila_prioridade.py')
    pdf.p(
        'Após o NLP processar a busca, ela é inserida na fila de prioridade. Buscas '
        'mais específicas (com mais filtros) recebem maior prioridade e são processadas '
        'primeiro, melhorando a eficiência do sistema.'
    )
    pdf.p('Implementada com heapq (min-heap com negação de prioridade para simular max-heap).')
    pdf.box(
        'Critérios de pontuação',
        '+3 pontos — categoria identificada (celular, notebook, tv…)\n'
        '+2 pontos — faixa de preço identificada (baixo, médio, alto)\n'
        '+2 pontos — marca identificada (Samsung, Apple, Sony…)\n'
        '+1 ponto  — por cada atributo identificado (câmera, bateria…)'
    )

    pdf.add_page()
    pdf.h2('3.3  Pilha (Stack — LIFO)')
    pdf.p('Arquivo: estruturas/pilha.py')
    pdf.p(
        'Armazena o histórico de buscas do usuário. Permite navegar para buscas anteriores '
        '(funcionalidade "Voltar") e gera recomendações baseadas nos padrões de busca '
        'recentes. Capacidade configurável (padrão: 50 entradas).'
    )
    pdf.p('Implementada com collections.deque(maxlen=capacidade) — remoção automática O(1).')
    pdf.li('push(item): empilha a busca atual')
    pdf.li('pop(): remove e retorna o item do topo')
    pdf.li('voltar(): descarta a busca atual e retorna a anterior')
    pdf.li('historico(n): retorna as últimas n buscas')
    pdf.li('categorias_recentes(n): retorna as categorias das últimas n buscas')

    pdf.h2('3.4  Hash Table (Tabela de Dispersão)')
    pdf.p('Arquivo: estruturas/hash_table.py')
    pdf.p(
        'Armazena o catálogo completo de produtos com acesso direto por ID em O(1) '
        'médio. Utiliza encadeamento (chaining) para resolver colisões. Capacidade '
        'padrão de 100 buckets com fator de carga baixo dado o tamanho do catálogo.'
    )
    pdf.li('inserir(id, produto): armazena ou atualiza um produto — O(1) médio')
    pdf.li('buscar(id): acesso direto por ID — O(1) médio')
    pdf.li('buscar_por_atributo(campo, valor): filtro por qualquer campo — O(n)')
    pdf.li('listar_todos(), listar_chaves(), listar_itens(): enumeração completa')

    pdf.h2('3.5  Árvore de Categorias (N-ária)')
    pdf.p('Arquivo: estruturas/arvore.py')
    pdf.p(
        'Organiza os produtos em hierarquia de categorias, permitindo navegação e '
        'busca eficiente por ramos. A estrutura atual é: '
        'eletronico → celular / notebook / tv / fone / tablet / smartwatch / console / monitor.'
    )
    pdf.li('inserir(caminho, produto): insere produto no nó folha do caminho')
    pdf.li('buscar_categoria(caminho, filtros): retorna todos os produtos do ramo, com filtros opcionais')
    pdf.li('categoria_existe(caminho): verifica se um caminho de categorias existe')

    pdf.h2('3.6  Grafo de Produtos (Não-dirigido com Pesos)')
    pdf.p('Arquivo: estruturas/grafo.py')
    pdf.p(
        'Representa relações de co-compra entre produtos ("quem comprou X também '
        'comprou Y"). Cada aresta tem um peso entre 0.0 e 1.0 que indica a força '
        'da relação. Implementado como dicionário de adjacência.'
    )
    pdf.li('adicionar_relacao(a, b, peso): cria aresta bidirecional com peso')
    pdf.li('recomendar(id, top_n): retorna os top_n vizinhos de maior peso')
    pdf.li('recomendar_por_historico(ids): agrega vizinhos de múltiplos produtos do histórico')
    pdf.li('produto_existe(id), listar_relacoes(), grau(id): consultas estruturais')

    # ── NLP ─────────────────────────────────────────────────
    pdf.add_page()
    pdf.h1(4, 'NLP e Parser')
    pdf.p('Arquivo: nucleo/nlp_parser.py')
    pdf.p(
        'O NLPParser é responsável por interpretar a intenção do usuário a partir de '
        'texto livre. Funciona com correspondência de padrões (sem modelos de ML externos) '
        'e normalização de texto para lidar com acentos, plurais e variações de género.'
    )

    pdf.h2('Normalização')
    pdf.p(
        'Todo texto é normalizado antes da comparação: convertido para minúsculas e '
        'acentos removidos via unicodedata.normalize(). Isso garante que "câmera", '
        '"camera" e "CÂMERA" sejam tratados igualmente, e que "barata" corresponda '
        'a "barato".'
    )

    pdf.h2('Campos extraídos')
    pdf.tabela(
        ['Campo', 'Exemplos reconhecidos', 'Resultado'],
        [
            ['tipo',      'quero, comprar, busco, versus, o que é',   'compra / comparar / informacao'],
            ['categoria', 'celular, celulares, smartphone, iphone',   'celular'],
            ['categoria', 'notebook, notebooks, laptop, pc',          'notebook'],
            ['categoria', 'tv, tvs, televisao, televisoes',           'tv'],
            ['categoria', 'tablet, tablets, ipad',                    'tablet'],
            ['categoria', 'console, ps5, xbox, nintendo',             'console'],
            ['preco',     'barato, barata, econômico, acessível',     'baixo'],
            ['preco',     'intermediário, médio, moderado',           'medio'],
            ['preco',     'premium, caro, cara, topo de linha',       'alto'],
            ['marca',     'samsung, apple, xiaomi, sony, dell',       'samsung / apple / …'],
            ['atributos', 'câmera, bateria, tela, memória',           'lista de atributos'],
        ],
        [35, 90, 41]
    )

    pdf.h2('Marcas reconhecidas (24)')
    marcas = [
        'samsung, apple, motorola, xiaomi, sony, lg, dell, acer, hp, asus,',
        'lenovo, positivo, jbl, beats, edifier, tcl, philips, nintendo, microsoft,',
        'garmin, amazfit, aoc, multilaser, realme'
    ]
    for m in marcas:
        pdf.p(m)

    # ── Catálogo ─────────────────────────────────────────────
    pdf.h1(5, 'Catálogo de Produtos')
    pdf.p('Arquivo: dados/catalogo.py')
    pdf.p(
        'O catálogo é um módulo separado com 49 produtos em 8 categorias. Cada produto '
        'tem um ID único, nome, categoria, marca, faixa de preço e valor em reais. '
        'As relações do grafo também são definidas aqui (40+ arestas).'
    )
    pdf.h2('Estrutura de um produto')
    pdf.box(
        'Campos de cada produto',
        "id       — identificador único (ex: 'cel003')\n"
        "nome     — nome comercial (ex: 'iPhone 15')\n"
        "categoria— grupo de produto (ex: 'celular')\n"
        "marca    — fabricante (ex: 'apple')\n"
        "preco    — faixa: 'baixo', 'medio' ou 'alto'\n"
        "valor    — preço em reais (ex: 5999.00)"
    )
    pdf.tabela(
        ['Categoria', 'Qtd.', 'Marcas presentes'],
        [
            ['celular',    '9', 'Motorola, Samsung, Apple, Xiaomi, Realme'],
            ['notebook',   '8', 'Acer, Dell, Apple, Lenovo, HP, ASUS, Samsung, Positivo'],
            ['tv',         '6', 'TCL, Samsung, LG, Philips, Sony, AOC'],
            ['fone',       '7', 'JBL, Sony, Beats, Edifier, Samsung, Apple, Multilaser'],
            ['tablet',     '5', 'Samsung, Apple, Lenovo'],
            ['smartwatch', '5', 'Xiaomi, Samsung, Apple, Amazfit, Garmin'],
            ['console',    '4', 'Nintendo, Sony, Microsoft'],
            ['monitor',    '5', 'AOC, LG, Dell, Samsung, Multilaser'],
        ],
        [40, 18, 108]
    )

    # ── Interface ────────────────────────────────────────────
    pdf.add_page()
    pdf.h1(6, 'Interface Web e Servidor')

    pdf.h2('Servidor HTTP (servidor.py)')
    pdf.p(
        'Servidor Python puro usando http.server.HTTPServer. Inicializa o '
        'AssistenteDeCompras uma vez e mantém o estado (histórico) entre requisições.'
    )
    pdf.tabela(
        ['Rota', 'Método', 'Descrição'],
        [
            ['/',        'GET', 'Serve o frontend (index.html)'],
            ['/buscar?q=', 'GET', 'Processa busca e retorna JSON com resultados e recomendações'],
            ['/voltar',  'GET', 'Retorna resultados da busca anterior (usa a Pilha)'],
        ],
        [45, 25, 96]
    )

    pdf.h2('Frontend (index.html)')
    pdf.p(
        'Interface web em HTML/CSS/JavaScript puro, sem frameworks externos. '
        'Design escuro com identidade visual roxa. Funcionalidades principais:'
    )
    pdf.li('Barra de busca com sugestões rápidas (chips de categorias)')
    pdf.li('Resultados separados em duas seções: Resultados diretos e Recomendados')
    pdf.li('Botão "Voltar" que usa o histórico da pilha para retornar à busca anterior')
    pdf.li('Mensagem de não encontrado com chips de categorias sugeridas')
    pdf.li('Ícones por categoria, badge de faixa de preço com cores distintas')
    pdf.li('Suporte a Enter na barra de busca e animação de entrada dos cards')

    # ── Estrutura de Arquivos ────────────────────────────────
    pdf.h1(7, 'Estrutura de Arquivos')
    pdf.box(
        'Organização do projeto',
        'Assistente-de-Compras-Inteligente/\n'
        '├── assistente.py          — classe principal AssistenteDeCompras\n'
        '├── servidor.py            — servidor HTTP com rotas /buscar e /voltar\n'
        '├── index.html             — interface web (frontend)\n'
        '├── dados/\n'
        '│   └── catalogo.py        — 49 produtos e 40+ relações do grafo\n'
        '├── estruturas/\n'
        '│   ├── fila_simples.py    — Fila FIFO com deque\n'
        '│   ├── fila_prioridade.py — Max-Heap com heapq\n'
        '│   ├── pilha.py           — Stack com deque(maxlen)\n'
        '│   ├── hash_table.py      — Tabela de dispersão com chaining\n'
        '│   ├── arvore.py          — Árvore N-ária de categorias\n'
        '│   └── grafo.py           — Grafo não-dirigido com pesos\n'
        '├── nucleo/\n'
        '│   └── nlp_parser.py      — Parser de linguagem natural\n'
        '└── testes/\n'
        '    ├── test_fila_simples.py\n'
        '    ├── test_fila_prioridade.py\n'
        '    ├── test_hash_table.py\n'
        '    ├── test_pilha.py\n'
        '    ├── teste_grafo.py\n'
        '    └── teste_arvore.py'
    )

    # ── Como Executar ─────────────────────────────────────────
    pdf.h1(8, 'Como Executar')
    pdf.p('Pré-requisito: Python 3.x instalado. Nenhuma biblioteca externa é necessária.')
    pdf.box(
        'Passos para iniciar',
        '1. Abra o terminal na pasta do projeto:\n'
        '   cd "Projeto Programação 2/Assistente-de-Compras-Inteligente"\n\n'
        '2. Execute o servidor:\n'
        '   python servidor.py\n\n'
        '3. O navegador abre automaticamente em http://localhost:8000\n\n'
        '4. Para parar o servidor: Ctrl+C no terminal'
    )
    pdf.h2('Executar os testes')
    pdf.box(
        'Rodar testes individuais',
        'python testes/test_fila_simples.py\n'
        'python testes/test_pilha.py\n'
        'python testes/test_hash_table.py\n'
        'python testes/teste_grafo.py\n'
        'python testes/teste_arvore.py'
    )

    saida = os.path.join(BASE, 'Documentacao_Tecnica.pdf')
    pdf.output(saida)
    print(f'  Gerado: {saida}')


# ─────────────────────────────────────────────────────────────
#  DOCUMENTO 2 — HISTÓRICO DE ALTERAÇÕES
# ─────────────────────────────────────────────────────────────
def doc_alteracoes():
    pdf = Doc('Assistente de Compras Inteligente — Histórico de Alterações')
    pdf.capa('Histórico de Alterações', 'Sessão de Desenvolvimento — 08/06/2026')

    # ── Resumo ───────────────────────────────────────────────
    pdf.add_page()
    pdf.h1(1, 'Resumo das Alterações')
    pdf.p(
        'Este documento registra todas as alterações realizadas durante a sessão de '
        'desenvolvimento de 08/06/2026. As mudanças abrangem correções de bugs, '
        'melhorias de performance, novas funcionalidades, expansão do catálogo e '
        'atualização dos testes.'
    )
    pdf.tabela(
        ['Categoria', 'Qtd. de mudanças'],
        [
            ['Correções de bugs',             '4'],
            ['Melhorias de performance',      '2'],
            ['Novas funcionalidades',         '7'],
            ['Expansão do catálogo',          '3'],
            ['Organização e limpeza',         '5'],
            ['Atualizações nos testes',       '4'],
        ],
        [120, 46]
    )

    # ── Bugs ─────────────────────────────────────────────────
    pdf.h1(2, 'Correções de Bugs')

    pdf.badge('BUG CRÍTICO', 'Pilha não inicializava — __init__ sem underscores duplos',
              'Arquivo: estruturas/pilha.py\n'
              'Problema: o método construtor estava definido como "def init()" em vez de '
              '"def __init__()". O Python nunca chamava o construtor, então self._dados '
              'nunca era criado. Qualquer chamada a push(), pop() ou historico() '
              'lançava AttributeError.\n'
              'Solução: corrigido para "def __init__(self, capacidade: int = 50)".')

    pdf.badge('BUG CRÍTICO', 'Servidor não respondia à rota /buscar — frontend não funcionava',
              'Arquivo: servidor.py\n'
              'Problema: o servidor usava SimpleHTTPRequestHandler puro, que só serve '
              'arquivos estáticos. O frontend fazia fetch("/buscar?q=...") e recebia 404.\n'
              'Solução: classe Handler estendida com método do_GET() que intercepta '
              '/buscar e /voltar, retornando JSON com os resultados.')

    pdf.badge('BUG', 'Busca por termos sem relação retornava todo o catálogo',
              'Arquivo: assistente.py\n'
              'Problema: quando o NLP não reconhecia categoria nem preço (ex: "cuscuz"), '
              'o método buscar() caia no else: catalogo.listar_todos(), retornando '
              'todos os 49 produtos. Além disso, _recomendar_por_historico() rodava '
              'e adicionava mais 2 itens baseados no histórico.\n'
              'Solução: retorno antecipado quando não há categoria, preço nem marca.')

    pdf.badge('BUG', 'Adjetivos no feminino não reconhecidos pelo NLP',
              'Arquivo: nucleo/nlp_parser.py\n'
              'Problema: "televisão barata" não filtrava por preço porque a lista de '
              'keywords tinha "barato" (masculino) mas não "barata" (feminino). '
              'Mesmo problema com "cara", "caras", "baratas", "econômica".\n'
              'Solução: adicionadas todas as formas: barata, baratas, econômica, '
              'cara, caras, média.')

    # ── Performance ──────────────────────────────────────────
    pdf.add_page()
    pdf.h1(3, 'Melhorias de Performance')

    pdf.badge('PERFORMANCE', 'FilaSimples: list.pop(0) → deque.popleft()',
              'Arquivo: estruturas/fila_simples.py\n'
              'Problema: list.pop(0) em Python é O(n) — desloca todos os elementos.\n'
              'Solução: substituído por collections.deque com popleft(), que é O(1). '
              'Para filas com volume alto de requisições, a diferença é significativa.')

    pdf.badge('PERFORMANCE', 'Pilha: list + pop(0) manual → deque(maxlen=capacidade)',
              'Arquivo: estruturas/pilha.py\n'
              'Problema: quando a pilha atingia a capacidade, fazia pop(0) para remover '
              'o item mais antigo — também O(n).\n'
              'Solução: deque com maxlen faz remoção automática do elemento mais antigo '
              'ao atingir o limite, em O(1).')

    # ── Novas Funcionalidades ─────────────────────────────────
    pdf.h1(4, 'Novas Funcionalidades')

    pdf.badge('FEATURE', 'Reconhecimento de marcas no NLP',
              'Arquivo: nucleo/nlp_parser.py\n'
              'Adicionado dicionário MARCAS com 24 fabricantes e seus termos de busca. '
              'O campo "marca" é agora extraído pelo parsear() e retornado no resultado.\n'
              'Exemplos: "samsung" → marca=samsung; "celular da apple" → '
              'categoria=celular + marca=apple; "moto" → marca=motorola.')

    pdf.badge('FEATURE', 'Campo marca nos produtos do catálogo',
              'Arquivo: dados/catalogo.py\n'
              'Todos os 49 produtos receberam o campo "marca" com o fabricante '
              'normalizado (ex: "apple", "samsung", "motorola"). Isso permite filtrar '
              'os resultados exatamente pela marca solicitada.')

    pdf.badge('FEATURE', 'Plurais de categorias reconhecidos',
              'Arquivo: nucleo/nlp_parser.py\n'
              'Adicionadas formas plurais em todas as categorias: "celulares", '
              '"notebooks", "tvs", "fones", "tablets", "smartwatches", "consoles", '
              '"monitores". Antes, buscas no plural retornavam vazio.')

    pdf.badge('FEATURE', 'Separação visual: Resultados vs Recomendados',
              'Arquivos: servidor.py, index.html\n'
              'O servidor passou a retornar JSON estruturado com dois campos separados: '
              '"resultados" (busca direta) e "recomendacoes" (grafo + histórico). '
              'O frontend exibe as duas seções com headers distintos, deixando '
              'claro para o usuário o que é resultado direto e o que é sugestão.')

    pdf.badge('FEATURE', 'Botão Voltar na interface web',
              'Arquivos: servidor.py (rota /voltar), index.html (botão + função JS)\n'
              'Implementado botão "← Voltar" que aparece após a primeira busca. '
              'Ao clicar, chama /voltar no servidor, que usa o método voltar() da '
              'Pilha para retornar aos resultados da busca anterior.')

    pdf.badge('FEATURE', 'Mensagem de não encontrado com sugestões',
              'Arquivo: index.html\n'
              'Quando a busca não retorna resultados, em vez de só "Nenhum produto '
              'encontrado", o sistema exibe chips clicáveis com todas as 8 categorias '
              'disponíveis, ajudando o usuário a reformular a busca.')

    pdf.badge('FEATURE', 'Recomendação por histórico exclui categoria atual',
              'Arquivo: assistente.py\n'
              'O método _recomendar_por_historico() passou a receber a categoria da '
              'busca atual como parâmetro. Ela é excluída da análise de histórico, '
              'evitando que produtos da mesma categoria apareçam como "recomendados" '
              'quando o usuário já está vendo todos eles nos resultados diretos.')

    # ── Catálogo ─────────────────────────────────────────────
    pdf.add_page()
    pdf.h1(5, 'Expansão do Catálogo')

    pdf.badge('REFACTOR', 'Catálogo movido para módulo separado dados/catalogo.py',
              'Antes: a lista de produtos e relações estava inline no método '
              '_popular_catalogo() em assistente.py, tornando o arquivo longo e difícil '
              'de manter.\n'
              'Depois: dados/catalogo.py contém PRODUTOS e RELACOES como constantes. '
              'assistente.py importa com "from dados.catalogo import PRODUTOS, RELACOES". '
              'Para adicionar produtos, basta editar catalogo.py sem tocar na lógica.')

    pdf.badge('EXPANSÃO', 'Catálogo: 11 → 49 produtos em 8 categorias',
              'Categorias adicionadas: tablet, smartwatch, console, monitor\n'
              'Produtos por categoria: celular(9), notebook(8), tv(6), fone(7), '
              'tablet(5), smartwatch(5), console(4), monitor(5)\n'
              'Relações no grafo: 7 → 40+ (celular↔fone, celular↔smartwatch, '
              'notebook↔monitor, console↔tv, tablet↔fone)')

    pdf.badge('EXPANSÃO', 'NLP atualizado para 8 categorias e 24 marcas',
              'Arquivo: nucleo/nlp_parser.py\n'
              'Adicionados keywords para: tablet, smartwatch, console, monitor.\n'
              'Adicionado dicionário MARCAS com: samsung, apple, motorola, xiaomi, '
              'sony, lg, dell, acer, hp, asus, lenovo, positivo, jbl, beats, edifier, '
              'tcl, philips, nintendo, microsoft, garmin, amazfit, aoc, multilaser, realme.')

    # ── Organização ──────────────────────────────────────────
    pdf.h1(6, 'Organização e Limpeza de Código')

    pdf.badge('LIMPEZA', 'Arquivos de código morto removidos',
              'Removidos: estruturas/none.py (classe Node incompleta sem uso) e '
              'main.py (rascunho de testes com lista crua). Nenhum dos dois era '
              'importado em lugar algum do projeto.')

    pdf.badge('LIMPEZA', 'Bloco __main__ removido de assistente.py',
              'O bloco "if __name__ == __main__" em assistente.py continha frases '
              'de teste com emojis que causavam problemas em terminais Windows. '
              'Foi removido — os testes adequados ficam na pasta testes/.')

    pdf.badge('LIMPEZA', 'Escrita desnecessária de data.js removida',
              'assistente.py escrevia um arquivo data.js a cada inicialização com '
              'os dados do catálogo. O frontend havia migrado para usar a API /buscar '
              'e não lia mais esse arquivo. A escrita foi removida, junto com os '
              'imports json e pathlib que só serviam para isso.')

    pdf.badge('REFACTOR', 'Servidor: método _json() extraído para evitar repetição',
              'Arquivo: servidor.py\n'
              'O código de serializar JSON e enviar a resposta HTTP era duplicado '
              'para cada rota. Extraído para o método auxiliar _json(dados) que '
              'centraliza Content-Type, Content-Length e Access-Control-Allow-Origin.')

    pdf.badge('MELHORIA', 'Normalização de acentos no NLP',
              'Arquivo: nucleo/nlp_parser.py\n'
              'Adicionado método estático _norm() usando unicodedata.normalize(NFD). '
              'Remove acentos antes de comparar keywords. "câmera" = "camera", '
              '"televisão" = "televisao", "econômico" = "economico". '
              'Todos os keywords do parser foram simplificados para a forma sem acento.')

    # ── Testes ───────────────────────────────────────────────
    pdf.add_page()
    pdf.h1(7, 'Atualizações nos Testes')

    pdf.badge('TESTES', 'test_fila_simples.py criado do zero',
              'Arquivo: testes/test_fila_simples.py\n'
              'O arquivo existia mas estava vazio (1 linha em branco). '
              'Criados 6 testes: enqueue/dequeue, ordem FIFO, esta_vazia, '
              'tamanho, exceção em fila vazia, repr.')

    pdf.badge('TESTES', 'Métodos novos adicionados em Pilha',
              'Arquivo: estruturas/pilha.py\n'
              'Adicionados para satisfazer test_pilha.py:\n'
              '- tamanho() → int\n'
              '- categorias_recentes(n) → lista de categorias das últimas n buscas\n'
              '- __repr__() → representação string')

    pdf.badge('TESTES', 'Métodos novos adicionados em HashTable',
              'Arquivo: estruturas/hash_table.py\n'
              'Adicionados para satisfazer test_hash_table.py:\n'
              '- listar_chaves() → lista de todas as chaves\n'
              '- listar_itens() → lista de tuplas (chave, valor)\n'
              '- __repr__() → representação string')

    pdf.badge('TESTES', 'Métodos novos adicionados em GrafoProdutos e ArvoreCategorias',
              'Arquivo: estruturas/grafo.py\n'
              '- produto_existe(id) → bool\n'
              '- listar_relacoes() → lista de tuplas (a, b, peso) sem duplicatas\n'
              '- recomendar_por_historico(ids) → recomendações agregadas de múltiplos produtos\n\n'
              'Arquivo: estruturas/arvore.py\n'
              '- buscar_categoria(caminho, filtros=None) → suporte a filtros opcionais\n'
              '- categoria_existe(caminho) → bool')

    saida = os.path.join(BASE, 'Historico_Alteracoes.pdf')
    pdf.output(saida)
    print(f'  Gerado: {saida}')


if __name__ == '__main__':
    print('Gerando PDFs...')
    doc_tecnica()
    doc_alteracoes()
    print('Concluído!')
