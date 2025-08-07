from bottle import Bottle, static_file

routes_static = Bottle()

@routes_static.route('/static/<filepath:path>')
def serve_static(filepath):
    """
    Rota para servir arquivos estáticos como CSS, JS, imagens, fontes e Bootstrap.

    Parâmetros:
        filepath (str): Caminho relativo do arquivo dentro da pasta 'static/'.

    Retorna:
        static_file: Arquivo localizado em 'static/<filepath>'.
    """
    return static_file(filepath, root='static')

@routes_static.route('/data/<filename>')
def serve_data_images(filename):
    """
    Rota para servir arquivos de dados ou imagens geradas dinamicamente (ex: gráficos).

    Parâmetros:
        filename (str): Nome do arquivo localizado na pasta 'data/'.

    Retorna:
        static_file: Arquivo localizado em 'data/<filename>'.
    """
    return static_file(filename, root='data')