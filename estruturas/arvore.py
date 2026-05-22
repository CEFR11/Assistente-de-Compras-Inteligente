class NoArvore:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = {}
        self.produtos = []

class ArvoreCategorias:
    def __init__(self):
        self.raiz = NoArvore('raiz')

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

    def _coletar(self, no):
        resultado = list(no.produtos)
        for filho in no.filhos.values():
            resultado.extend(self._coletar(filho))
        return resultado