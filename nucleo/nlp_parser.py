class NLPParser:
    """Módulo compartilhado – interpreta entrada em linguagem natural."""
    CATEGORIAS = {
        'celular':  ['celular', 'smartphone', 'iphone', 'android', 'telefone'],
        'notebook': ['notebook', 'laptop', 'computador', 'pc'],
        'tv':       ['tv', 'televisão', 'televisor', 'tela grande'],
        'fone':     ['fone', 'headphone', 'earphone', 'airpod', 'fones'],
    }
    PRECOS = {
        'baixo': ['barato', 'econômico', 'acessível', 'custo-benefício', 'em conta'],
        'medio': ['intermediário', 'moderado', 'médio'],
        'alto':  ['premium', 'caro', 'topo de linha', 'top', 'melhor'],
    }
    ATRIBUTOS = ['câmera', 'bateria', 'tela', 'memória', 'armazenamento',
                 'velocidade', 'desempenho', 'resistente', 'leve', 'fino']
    TIPOS = {
        'comparar':  ['comparar', 'diferença', 'melhor entre', 'qual é melhor', 'versus', 'vs'],
        'informacao': ['o que é', 'como funciona', 'me explica', 'me fala sobre'],
        'compra':    ['quero', 'comprar', 'busco', 'preciso', 'procuro', 'encontrar'],
    }

    def parsear(self, texto: str) -> dict:
        texto = texto.lower()
        resultado = {
            'original':  texto,
            'tipo':      'compra',
            'categoria': None,
            'preco':     None,
            'atributos': []
        }
        for tipo, palavras in self.TIPOS.items():
            if any(p in texto for p in palavras):
                resultado['tipo'] = tipo
                break
        for cat, palavras in self.CATEGORIAS.items():
            if any(p in texto for p in palavras):
                resultado['categoria'] = cat
                break
        for nivel, palavras in self.PRECOS.items():
            if any(p in texto for p in palavras):
                resultado['preco'] = nivel
                break
        resultado['atributos'] = [a for a in self.ATRIBUTOS if a in texto]
        return resultado