PRODUTOS = [
    # ── Celulares ──────────────────────────────────────────────────────────
    {'id': 'cel001', 'nome': 'Moto G54',              'categoria': 'celular',    'marca': 'motorola',  'preco': 'baixo', 'valor':  899.00, 'atributos': ['camera', 'bateria']},
    {'id': 'cel002', 'nome': 'Samsung Galaxy A35',     'categoria': 'celular',    'marca': 'samsung',   'preco': 'medio', 'valor': 1699.00, 'atributos': ['camera', 'tela', 'bateria']},
    {'id': 'cel003', 'nome': 'iPhone 15',              'categoria': 'celular',    'marca': 'apple',     'preco': 'alto',  'valor': 5999.00, 'atributos': ['camera', 'desempenho', 'fino']},
    {'id': 'cel004', 'nome': 'Xiaomi Redmi 13C',       'categoria': 'celular',    'marca': 'xiaomi',    'preco': 'baixo', 'valor':  699.00, 'atributos': ['bateria', 'tela']},
    {'id': 'cel005', 'nome': 'Samsung Galaxy S24',     'categoria': 'celular',    'marca': 'samsung',   'preco': 'alto',  'valor': 4499.00, 'atributos': ['camera', 'desempenho', 'tela']},
    {'id': 'cel006', 'nome': 'Motorola Edge 40',       'categoria': 'celular',    'marca': 'motorola',  'preco': 'medio', 'valor': 2199.00, 'atributos': ['camera', 'bateria', 'fino']},
    {'id': 'cel007', 'nome': 'Poco X6 Pro',            'categoria': 'celular',    'marca': 'xiaomi',    'preco': 'medio', 'valor': 1899.00, 'atributos': ['desempenho', 'bateria', 'camera']},
    {'id': 'cel008', 'nome': 'iPhone 15 Pro Max',      'categoria': 'celular',    'marca': 'apple',     'preco': 'alto',  'valor': 8999.00, 'atributos': ['camera', 'desempenho', 'tela', 'fino']},
    {'id': 'cel009', 'nome': 'Realme C55',             'categoria': 'celular',    'marca': 'realme',    'preco': 'baixo', 'valor':  799.00, 'atributos': ['bateria', 'camera']},
    # ── Notebooks ──────────────────────────────────────────────────────────
    {'id': 'nb001',  'nome': 'Acer Aspire 3',          'categoria': 'notebook',   'marca': 'acer',      'preco': 'baixo', 'valor': 2199.00, 'atributos': ['memoria', 'armazenamento']},
    {'id': 'nb002',  'nome': 'Dell Inspiron 15',        'categoria': 'notebook',   'marca': 'dell',      'preco': 'medio', 'valor': 3499.00, 'atributos': ['desempenho', 'tela', 'memoria']},
    {'id': 'nb003',  'nome': 'MacBook Air M2',          'categoria': 'notebook',   'marca': 'apple',     'preco': 'alto',  'valor': 9999.00, 'atributos': ['desempenho', 'leve', 'fino', 'bateria']},
    {'id': 'nb004',  'nome': 'Lenovo IdeaPad 3',        'categoria': 'notebook',   'marca': 'lenovo',    'preco': 'baixo', 'valor': 2499.00, 'atributos': ['memoria', 'armazenamento']},
    {'id': 'nb005',  'nome': 'HP Victus 15',            'categoria': 'notebook',   'marca': 'hp',        'preco': 'medio', 'valor': 4299.00, 'atributos': ['desempenho', 'memoria', 'velocidade']},
    {'id': 'nb006',  'nome': 'ASUS ROG Zephyrus G14',   'categoria': 'notebook',   'marca': 'asus',      'preco': 'alto',  'valor': 12999.00,'atributos': ['desempenho', 'velocidade', 'tela']},
    {'id': 'nb007',  'nome': 'Samsung Book2 Pro',       'categoria': 'notebook',   'marca': 'samsung',   'preco': 'alto',  'valor': 7499.00, 'atributos': ['leve', 'fino', 'tela', 'bateria']},
    {'id': 'nb008',  'nome': 'Positivo Motion C41TBi',  'categoria': 'notebook',   'marca': 'positivo',  'preco': 'baixo', 'valor': 1799.00, 'atributos': ['memoria']},
    # ── TVs ────────────────────────────────────────────────────────────────
    {'id': 'tv001',  'nome': 'TV TCL 43" 4K',           'categoria': 'tv',         'marca': 'tcl',       'preco': 'baixo', 'valor': 1299.00, 'atributos': ['tela']},
    {'id': 'tv002',  'nome': 'Samsung 55" QLED',         'categoria': 'tv',         'marca': 'samsung',   'preco': 'alto',  'valor': 4799.00, 'atributos': ['tela', 'desempenho']},
    {'id': 'tv003',  'nome': 'LG 50" NanoCell',          'categoria': 'tv',         'marca': 'lg',        'preco': 'medio', 'valor': 2499.00, 'atributos': ['tela']},
    {'id': 'tv004',  'nome': 'Philips 32" HD',           'categoria': 'tv',         'marca': 'philips',   'preco': 'baixo', 'valor':  899.00, 'atributos': ['tela']},
    {'id': 'tv005',  'nome': 'Sony 65" Bravia XR',       'categoria': 'tv',         'marca': 'sony',      'preco': 'alto',  'valor': 6999.00, 'atributos': ['tela', 'desempenho']},
    {'id': 'tv006',  'nome': 'AOC 40" Full HD',          'categoria': 'tv',         'marca': 'aoc',       'preco': 'baixo', 'valor': 1099.00, 'atributos': ['tela']},
    # ── Fones ──────────────────────────────────────────────────────────────
    {'id': 'fone001','nome': 'JBL Tune 510BT',           'categoria': 'fone',       'marca': 'jbl',       'preco': 'baixo', 'valor':  249.00, 'atributos': ['bateria']},
    {'id': 'fone002','nome': 'Sony WH-1000XM5',          'categoria': 'fone',       'marca': 'sony',      'preco': 'alto',  'valor': 2199.00, 'atributos': ['bateria', 'desempenho']},
    {'id': 'fone003','nome': 'Beats Studio Pro',         'categoria': 'fone',       'marca': 'beats',     'preco': 'alto',  'valor': 1899.00, 'atributos': ['desempenho', 'bateria']},
    {'id': 'fone004','nome': 'Edifier W820NB',           'categoria': 'fone',       'marca': 'edifier',   'preco': 'medio', 'valor':  549.00, 'atributos': ['bateria', 'desempenho']},
    {'id': 'fone005','nome': 'Samsung Galaxy Buds2',     'categoria': 'fone',       'marca': 'samsung',   'preco': 'medio', 'valor':  699.00, 'atributos': ['bateria', 'leve']},
    {'id': 'fone006','nome': 'AirPods Pro 2a Geracao',   'categoria': 'fone',       'marca': 'apple',     'preco': 'alto',  'valor': 2499.00, 'atributos': ['desempenho', 'leve', 'bateria']},
    {'id': 'fone007','nome': 'Multilaser PH341',         'categoria': 'fone',       'marca': 'multilaser','preco': 'baixo', 'valor':   89.00, 'atributos': []},
    # ── Tablets ────────────────────────────────────────────────────────────
    {'id': 'tab001', 'nome': 'Samsung Galaxy Tab A9',    'categoria': 'tablet',     'marca': 'samsung',   'preco': 'baixo', 'valor': 1299.00, 'atributos': ['tela', 'bateria']},
    {'id': 'tab002', 'nome': 'iPad 10a Geracao',         'categoria': 'tablet',     'marca': 'apple',     'preco': 'medio', 'valor': 3999.00, 'atributos': ['tela', 'desempenho']},
    {'id': 'tab003', 'nome': 'iPad Pro M4',              'categoria': 'tablet',     'marca': 'apple',     'preco': 'alto',  'valor': 9999.00, 'atributos': ['tela', 'desempenho', 'fino', 'leve']},
    {'id': 'tab004', 'nome': 'Lenovo Tab M10 Plus',      'categoria': 'tablet',     'marca': 'lenovo',    'preco': 'baixo', 'valor':  999.00, 'atributos': ['tela', 'bateria']},
    {'id': 'tab005', 'nome': 'Samsung Galaxy Tab S9',    'categoria': 'tablet',     'marca': 'samsung',   'preco': 'alto',  'valor': 5999.00, 'atributos': ['tela', 'desempenho', 'camera']},
    # ── Smartwatches ───────────────────────────────────────────────────────
    {'id': 'sw001',  'nome': 'Xiaomi Smart Band 8',      'categoria': 'smartwatch', 'marca': 'xiaomi',    'preco': 'baixo', 'valor':  299.00, 'atributos': ['bateria', 'leve', 'resistente']},
    {'id': 'sw002',  'nome': 'Samsung Galaxy Watch 6',   'categoria': 'smartwatch', 'marca': 'samsung',   'preco': 'medio', 'valor': 1499.00, 'atributos': ['tela', 'bateria', 'desempenho']},
    {'id': 'sw003',  'nome': 'Apple Watch Series 9',     'categoria': 'smartwatch', 'marca': 'apple',     'preco': 'alto',  'valor': 3999.00, 'atributos': ['tela', 'desempenho', 'bateria']},
    {'id': 'sw004',  'nome': 'Amazfit GTS 4 Mini',       'categoria': 'smartwatch', 'marca': 'amazfit',   'preco': 'baixo', 'valor':  499.00, 'atributos': ['bateria', 'leve', 'resistente']},
    {'id': 'sw005',  'nome': 'Garmin Forerunner 265',    'categoria': 'smartwatch', 'marca': 'garmin',    'preco': 'alto',  'valor': 3299.00, 'atributos': ['bateria', 'resistente', 'desempenho', 'tela']},
    # ── Consoles ───────────────────────────────────────────────────────────
    {'id': 'con001', 'nome': 'Nintendo Switch Lite',     'categoria': 'console',    'marca': 'nintendo',  'preco': 'baixo', 'valor': 1799.00, 'atributos': ['bateria', 'leve']},
    {'id': 'con002', 'nome': 'PlayStation 5',            'categoria': 'console',    'marca': 'sony',      'preco': 'alto',  'valor': 4499.00, 'atributos': ['desempenho', 'velocidade', 'armazenamento']},
    {'id': 'con003', 'nome': 'Xbox Series S',            'categoria': 'console',    'marca': 'microsoft', 'preco': 'medio', 'valor': 2299.00, 'atributos': ['desempenho', 'armazenamento']},
    {'id': 'con004', 'nome': 'Nintendo Switch OLED',     'categoria': 'console',    'marca': 'nintendo',  'preco': 'medio', 'valor': 2799.00, 'atributos': ['tela', 'bateria', 'leve']},
    # ── Monitores ──────────────────────────────────────────────────────────
    {'id': 'mon001', 'nome': 'Monitor AOC 24" FHD',      'categoria': 'monitor',    'marca': 'aoc',       'preco': 'baixo', 'valor':  799.00, 'atributos': ['tela']},
    {'id': 'mon002', 'nome': 'LG UltraWide 29"',         'categoria': 'monitor',    'marca': 'lg',        'preco': 'medio', 'valor': 1899.00, 'atributos': ['tela']},
    {'id': 'mon003', 'nome': 'Dell 4K 27"',              'categoria': 'monitor',    'marca': 'dell',      'preco': 'alto',  'valor': 3999.00, 'atributos': ['tela', 'desempenho']},
    {'id': 'mon004', 'nome': 'Samsung Odyssey G5 32"',   'categoria': 'monitor',    'marca': 'samsung',   'preco': 'medio', 'valor': 2299.00, 'atributos': ['tela', 'desempenho', 'velocidade']},
    {'id': 'mon005', 'nome': 'Monitor Multilaser 21"',   'categoria': 'monitor',    'marca': 'multilaser','preco': 'baixo', 'valor':  599.00, 'atributos': ['tela']},
]

RELACOES = [
    # Celulares entre si
    ('cel001', 'cel002', 0.8), ('cel002', 'cel003', 0.6), ('cel004', 'cel001', 0.7),
    ('cel005', 'cel003', 0.9), ('cel006', 'cel007', 0.6), ('cel002', 'cel007', 0.5),
    ('cel008', 'cel005', 0.8), ('cel009', 'cel004', 0.7),
    # Celular <-> Fone
    ('fone001', 'cel001', 0.9), ('fone002', 'cel003', 0.85),
    ('fone003', 'cel005', 0.8), ('fone004', 'cel006', 0.7),
    ('fone005', 'cel002', 0.85), ('fone006', 'cel008', 0.95),
    # Celular <-> Smartwatch
    ('sw001', 'cel004', 0.8), ('sw002', 'cel002', 0.75),
    ('sw003', 'cel003', 0.9), ('sw003', 'cel005', 0.85),
    ('sw004', 'cel006', 0.7), ('sw005', 'cel008', 0.8),
    # Notebooks entre si
    ('nb001', 'nb002', 0.5), ('nb002', 'nb003', 0.6), ('nb004', 'nb001', 0.6),
    ('nb005', 'nb002', 0.7), ('nb006', 'nb003', 0.5), ('nb007', 'nb003', 0.6),
    ('nb008', 'nb001', 0.7),
    # Notebook <-> Monitor
    ('mon001', 'nb001', 0.8), ('mon002', 'nb002', 0.75),
    ('mon003', 'nb003', 0.85), ('mon004', 'nb005', 0.8),
    # Notebook <-> Tablet
    ('nb003', 'tab003', 0.7), ('tab002', 'nb002', 0.5), ('tab005', 'nb007', 0.6),
    # TVs entre si
    ('tv001', 'tv003', 0.5), ('tv002', 'tv005', 0.6), ('tv003', 'tv002', 0.6),
    ('tv004', 'tv001', 0.5), ('tv006', 'tv001', 0.6),
    # Console <-> TV
    ('con001', 'tv001', 0.8), ('con002', 'tv002', 0.9),
    ('con003', 'tv003', 0.85), ('con004', 'tv003', 0.8),
    # Tablets entre si
    ('tab001', 'tab002', 0.6), ('tab002', 'tab003', 0.5), ('tab004', 'tab001', 0.7),
    # Tablet <-> Fone
    ('tab001', 'fone001', 0.7), ('tab003', 'fone002', 0.8), ('tab005', 'fone006', 0.85),
]
