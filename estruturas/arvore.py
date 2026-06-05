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

    def buscar_categoria(self, caminho: list) -> list:
        
        no = self.raiz
        for categoria in caminho:
            if categoria not in no.filhos:
                return []
            no = no.filhos[categoria]
        return self._coletar(no)

    def _coletar(self, no) -> list:
        resultado = list(no.produtos)
        for filho in no.filhos.values():
            resultado.extend(self._coletar(filho))
        return resultado