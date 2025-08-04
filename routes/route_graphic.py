from bottle import Bottle, template
from ibge.api_ibge import get_indicadores
from utils.plot import plotar_graficos
import pandas as pd

route_graphics = Bottle()

@route_graphics.route('/')
def index():
    dados = get_indicadores()

    if not dados:
        return template('index', titulo = 'Erro', imagens = [])
    
    imagens = []

    try:
        chegada_de_turistas = dados[0]['series'][0]['series']
        turistas = []
        for item in chegada_de_turistas:
            for chave, valor in item.items():
                if valor is not None and chave != '-':
                    turistas.append((int(chave), float(valor)))

        df_chegada_turistas = pd.DataFrame(turistas)        

        plotar_graficos(
            df_chegada_turistas[0],
            df_chegada_turistas[1],
            "Economia - Chegada de Turistas - IBGE",
            "Ano",
            "(Em Milhões)",
            "grafico_turismo.png"
        )   

        imagens.append("/static/data/grafico_turismo.png") 

    except Exception as e:
        print(f"Erro - Falha no processamento de dados: {e}") 
        return template('index', titulo = "Erro", imagens = []) 

    return template('index', titulo = 'Indicadores Econômicos - IBGE', imagens = imagens)      