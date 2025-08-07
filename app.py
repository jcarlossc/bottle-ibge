from bottle import Bottle, run
from routes.routes_graficos import routes_graficos
from routes.routes_static import routes_static

# Criação da aplicação principal Bottle.
app = Bottle()

# Monta as rotas estáticas na subpasta /static
app.mount('/static', routes_static)

# Monta as rotas principais da aplicação (geração de gráficos) na raiz "/".
app.mount('/', routes_graficos)

# Também monta as rotas para arquivos de dados e imagens em /data
app.mount('/data', routes_static)

if __name__ == "__main__":
    """
    Ponto de entrada da aplicação web Bottle.

    Executa o servidor local em:
        - Host: localhost
        - Porta: 8080

    Parâmetros do servidor:
        - debug=True: ativa o modo de depuração (útil durante o desenvolvimento).
        - reloader=True: reinicia automaticamente o servidor ao detectar mudanças no código.
    """
    run(app, host='localhost', port=8080, debug=True, reloader=True)

