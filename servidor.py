import http.server
import webbrowser
import threading
import pathlib

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(pathlib.Path(__file__).parent), **kw)

if __name__ == '__main__':
    threading.Timer(0.5, lambda: webbrowser.open('http://localhost:8000')).start()
    server = http.server.HTTPServer(('localhost', 8000), Handler)
    print('🚀 Servidor rodando em http://localhost:8000')
    server.serve_forever()