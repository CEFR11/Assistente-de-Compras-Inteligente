class NoArvore:
    def __init__(self, nome: str):
        self.nome = nome
        self.filhos = {}
        self.produtos = []


class ArvoreCategorias:

    def __init__(self):
        self.raiz = NoArvore('raiz')

    def inserir(self, caminho: list, produto: dict):
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                no.filhos[categoria] = NoArvore(categoria)
            no = no.filhos[categoria]
        no.produtos.append(produto)

    def buscar_categoria(self, caminho: list, filtros: dict = None) -> list:
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                return []
            no = no.filhos[categoria]
        resultado = self._coletar(no)
        if filtros:
            for campo, valor in filtros.items():
                resultado = [p for p in resultado if p.get(campo) == valor]
        return resultado

    def categoria_existe(self, caminho: list) -> bool:
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                return False
            no = no.filhos[categoria]
        return True

    def _coletar(self, no) -> list:
        resultado = list(no.produtos)
        for filho in no.filhos.values():
            resultado.extend(self._coletar(filho))
        return resultado
