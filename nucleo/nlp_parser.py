import unicodedata

class NLPParser:
    CATEGORIAS = {
        'celular':    ['celular', 'celulares', 'smartphone', 'smartphones', 'iphone', 'android', 'telefone', 'telefones'],
        'notebook':   ['notebook', 'notebooks', 'laptop', 'laptops', 'computador', 'computadores', 'pc'],
        'tv':         ['tv', 'tvs', 'televisao', 'televisoes', 'televisor', 'televisores', 'tela grande'],
        'fone':       ['fone', 'fones', 'headphone', 'headphones', 'earphone', 'earphones', 'airpod', 'airpods'],
        'tablet':     ['tablet', 'tablets', 'ipad', 'ipads', 'tab'],
        'smartwatch': ['smartwatch', 'smartwatches', 'relogio', 'relogios', 'watch', 'pulseira', 'smart band'],
        'console':    ['console', 'consoles', 'videogame', 'videogames', 'playstation', 'xbox', 'nintendo', 'ps5', 'switch'],
        'monitor':    ['monitor', 'monitores', 'tela para pc', 'display'],
    }
    PRECOS = {
        'baixo': ['barato', 'barata', 'baratos', 'baratas', 'economico', 'economica', 'acessivel', 'custo-beneficio', 'em conta'],
        'medio': ['intermediario', 'moderado', 'medio', 'media'],
        'alto':  ['premium', 'caro', 'cara', 'caros', 'caras', 'topo de linha', 'top', 'melhor'],
    }
    ATRIBUTOS = ['camera', 'bateria', 'tela', 'memoria', 'armazenamento',
                 'velocidade', 'desempenho', 'resistente', 'leve', 'fino']
    TIPOS = {
        'comparar':   ['comparar', 'diferenca', 'melhor entre', 'qual e melhor', 'versus', 'vs'],
        'informacao': ['o que e', 'como funciona', 'me explica', 'me fala sobre'],
        'compra':     ['quero', 'comprar', 'busco', 'preciso', 'procuro', 'encontrar'],
    }
    MARCAS = {
        'samsung':    ['samsung'],
        'apple':      ['apple'],
        'motorola':   ['motorola', 'moto'],
        'xiaomi':     ['xiaomi', 'redmi', 'poco'],
        'sony':       ['sony'],
        'lg':         ['lg'],
        'dell':       ['dell'],
        'acer':       ['acer'],
        'hp':         ['hp'],
        'asus':       ['asus', 'rog'],
        'lenovo':     ['lenovo'],
        'positivo':   ['positivo'],
        'jbl':        ['jbl'],
        'beats':      ['beats'],
        'edifier':    ['edifier'],
        'tcl':        ['tcl'],
        'philips':    ['philips'],
        'nintendo':   ['nintendo'],
        'microsoft':  ['xbox', 'microsoft'],
        'garmin':     ['garmin'],
        'amazfit':    ['amazfit'],
        'aoc':        ['aoc'],
        'multilaser': ['multilaser'],
        'realme':     ['realme'],
    }

    @staticmethod
    def _norm(texto: str) -> str:
        return unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('ascii').lower()

    def parsear(self, texto: str) -> dict:
        texto_norm = self._norm(texto)
        resultado = {
            'original':  texto.lower(),
            'tipo':      'compra',
            'categoria': None,
            'preco':     None,
            'marca':     None,
            'atributos': []
        }
        for tipo, palavras in self.TIPOS.items():
            if any(p in texto_norm for p in palavras):
                resultado['tipo'] = tipo
                break
        for cat, palavras in self.CATEGORIAS.items():
            if any(p in texto_norm for p in palavras):
                resultado['categoria'] = cat
                break
        for nivel, palavras in self.PRECOS.items():
            if any(p in texto_norm for p in palavras):
                resultado['preco'] = nivel
                break
        for marca, palavras in self.MARCAS.items():
            if any(p in texto_norm for p in palavras):
                resultado['marca'] = marca
                break
        resultado['atributos'] = [a for a in self.ATRIBUTOS if a in texto_norm]
        return resultado
