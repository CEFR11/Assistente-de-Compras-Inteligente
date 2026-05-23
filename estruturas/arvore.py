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

    def buscar_categoria(self, caminho):
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                return []
            no = no.filhos[categoria]
        return self._coletar(no)

    def listar_categorias(self):
        resultado = []
        self._percorrer(self.raiz, [], resultado)
        return resultado

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