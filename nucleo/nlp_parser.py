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

    _MAPA_ACENTOS = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c', 'ñ': 'n',
        'Á': 'a', 'À': 'a', 'Ã': 'a', 'Â': 'a', 'Ä': 'a',
        'É': 'e', 'È': 'e', 'Ê': 'e', 'Ë': 'e',
        'Í': 'i', 'Ì': 'i', 'Î': 'i', 'Ï': 'i',
        'Ó': 'o', 'Ò': 'o', 'Õ': 'o', 'Ô': 'o', 'Ö': 'o',
        'Ú': 'u', 'Ù': 'u', 'Û': 'u', 'Ü': 'u',
        'Ç': 'c', 'Ñ': 'n',
    }

    @staticmethod
    def _norm(texto: str) -> str:
        resultado = texto.lower()
        for acento, simples in NLPParser._MAPA_ACENTOS.items():
            resultado = resultado.replace(acento, simples)
        return resultado

    @staticmethod
    def _levenshtein(s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        if abs(m - n) > 3:
            return abs(m - n)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                custo = 0 if s1[i - 1] == s2[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + custo,
                )
                if i > 1 and j > 1 and s1[i-1] == s2[j-2] and s1[i-2] == s2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-2][j-2] + 1)
        return dp[m][n]

    def _tem_match(self, texto_norm: str, palavras: list) -> bool:
        if any(p in texto_norm for p in palavras):
            return True
        for w in texto_norm.split():
            if len(w) < 3:
                continue
            for kw in palavras:
                if len(kw) < 3:
                    continue
                limite = 1 if len(kw) <= 5 else 2
                if self._levenshtein(w, kw) <= limite:
                    return True
        return False

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
            if self._tem_match(texto_norm, palavras):
                resultado['tipo'] = tipo
                break
        for cat, palavras in self.CATEGORIAS.items():
            if self._tem_match(texto_norm, palavras):
                resultado['categoria'] = cat
                break
        for nivel, palavras in self.PRECOS.items():
            if self._tem_match(texto_norm, palavras):
                resultado['preco'] = nivel
                break
        for marca, palavras in self.MARCAS.items():
            if self._tem_match(texto_norm, palavras):
                resultado['marca'] = marca
                break
        resultado['atributos'] = [a for a in self.ATRIBUTOS if self._tem_match(texto_norm, [a])]
        return resultado
