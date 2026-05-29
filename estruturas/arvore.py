class NoArvore:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = {}
        self.produtos = []

class ArvoreCategorias:
    def __init__(self):
        self.raiz = NoArvore('raiz')
        self._popular_categorias()

    def _popular_categorias(self):
        categorias = [
            ['Eletrônicos', 'Celulares'],
            ['Eletrônicos', 'Notebooks'],
            ['Eletrônicos', 'Televisores'],
            ['Eletrônicos', 'Fones'],
            ['Eletrodomésticos', 'Geladeiras'],
            ['Eletrodomésticos', 'Micro-ondas'],
            ['Eletrodomésticos', 'Máquinas de Lavar'],
            ['Moda', 'Masculino'],
            ['Moda', 'Feminino'],
            ['Moda', 'Calçados'],
            ['Esportes', 'Musculação'],
            ['Esportes', 'Corrida'],
            ['Esportes', 'Futebol'],
            ['Games', 'Consoles'],
            ['Games', 'Acessórios'],
        ]
        for caminho in categorias:
            self._criar_caminho(caminho)

    def _criar_caminho(self, caminho):
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                no.filhos[categoria] = NoArvore(categoria)
            no = no.filhos[categoria]

    def inserir(self, caminho, produto):
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                no.filhos[categoria] = NoArvore(categoria)
            no = no.filhos[categoria]
        no.produtos.append(produto)

    def buscar_categoria(self, caminho, filtros=None):
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                return []
            no = no.filhos[categoria]
        produtos = self._coletar(no)
        if filtros:
            produtos = self._refinar(produtos, filtros)
        return produtos

    def _refinar(self, produtos, filtros):
        resultado = []
        for produto in produtos:
            if all(produto.get(chave) == valor for chave, valor in filtros.items()):
                resultado.append(produto)
        return resultado

    def listar_categorias(self):
        resultado = []
        self._percorrer(self.raiz, [], resultado)
        return resultado

    def categoria_existe(self, caminho):
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                return False
            no = no.filhos[categoria]
        return True

    def _percorrer(self, no, caminho_atual, resultado):
        if caminho_atual:
            resultado.append(' > '.join(caminho_atual))
        for nome, filho in no.filhos.items():
            self._percorrer(filho, caminho_atual + [nome], resultado)

    def _coletar(self, no):
        resultado = list(no.produtos)
        for filho in no.filhos.values():
            resultado.extend(self._coletar(filho))
        return resultado