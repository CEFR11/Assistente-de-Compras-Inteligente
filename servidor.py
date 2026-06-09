import http.server
import webbrowser
import threading
import pathlib
import json
import sys
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from assistente import AssistenteDeCompras

assistente = AssistenteDeCompras()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(pathlib.Path(__file__).parent), **kw)

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == '/buscar':
            params = parse_qs(parsed.query)
            q = params.get('q', [''])[0].strip()
            if q:
                resultado = assistente.buscar(q)
                resposta = {
                    'resultados':    resultado['por_categoria'],
                    'recomendacoes': resultado['recomendacoes'],
                }
            else:
                resposta = {'resultados': [], 'recomendacoes': []}
            self._json(resposta)

        elif parsed.path == '/voltar':
            resultado = assistente.voltar()
            if resultado:
                resposta = {
                    'resultados':    resultado['por_categoria'],
                    'recomendacoes': resultado['recomendacoes'],
                }
            else:
                resposta = {'resultados': [], 'recomendacoes': [], 'vazio': True}
            self._json(resposta)

        else:
            super().do_GET()

    def _json(self, dados: dict):
        body = json.dumps(dados, ensure_ascii=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', len(body))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    threading.Timer(0.5, lambda: webbrowser.open('http://localhost:8000')).start()
    server = http.server.HTTPServer(('localhost', 8000), Handler)
    print('Servidor rodando em http://localhost:8000')
    server.serve_forever()
