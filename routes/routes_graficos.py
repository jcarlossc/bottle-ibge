from bottle import Bottle, template
from ibge.api_ibge import get_indicadores
from utils.plot import plotar_grafico
import pandas as pd

# Subaplicação Bottle responsável por gerar gráficos com dados do IBGE.
routes_graficos = Bottle()

@routes_graficos.route('/')
def index():
    """
    Rota principal da aplicação, responsável por:
        - Obter os dados dos indicadores do Brasil a partir da API do IBGE.
        - Processar e converter os dados em dataframes.
        - Gerar gráficos com matplotlib a partir dos dados processados.
        - Renderizar o template HTML ('index.tpl') exibindo os gráficos gerados.

    Retorna:
        Página HTML renderizada com os gráficos ou mensagem de erro em caso de falha.

    """
    dados = get_indicadores()
    if not dados:
        return template('index', titulo="Erro", imagens=[])

    imagens = []

    try:
        # Gráfico 1: Chegada de turistas
        chegada_de_turistas = dados[0]['series'][0]['serie']
        turistas = [(int(k), float(v)) for d in chegada_de_turistas for k, v in d.items() if v and k != "-"]
        df1 = pd.DataFrame(turistas)
        plotar_grafico(df1[0], df1[1], "Chegada de Turistas - IBGE", "Ano", "(Em Milhões)", "grafico_turismo.png")
        imagens.append("/static/data/grafico_turismo.png")

        # Gráfico 2: Gastos públicos com educação
        gastos_com_educacao = dados[1]['series'][0]['serie']
        gastos_educacao = [(int(k), float(v)) for d in gastos_com_educacao for k, v in d.items() if v and k != "-"]
        df2 = pd.DataFrame(gastos_educacao)
        plotar_grafico(df2[0], df2[1], "Gastos públicos com Educação - IBGE", "Ano", "(Em Porcentagem do PIB)", "grafico_educacao.png")
        imagens.append("/static/data/grafico_educacao.png")
        
        # Gráfico 3: Gastos públicos com saúde
        dados_gastos_saude = dados[2]['series'][0]['serie']
        gastos_saude = [(int(k), float(v)) for d in dados_gastos_saude for k, v in d.items() if v and k != "-"]
        df2 = pd.DataFrame(gastos_saude)
        plotar_grafico(df2[0], df2[1], "Gastos públicos com Educação - IBGE", "Ano", "(Em Porcentagem do PIB)", "grafico_saude.png")
        imagens.append("/static/data/grafico_saude.png")
        
        # Gráfico 4: Gastos públicos com pesquisa e desenvolvimento
        dados_gastos_pesquisas = dados[3]['series'][0]['serie']
        gastos_pesquisa = [(int(k), float(v)) for d in dados_gastos_pesquisas for k, v in d.items() if v and k != "-"]
        df2 = pd.DataFrame(gastos_pesquisa)
        plotar_grafico(df2[0], df2[1], "Gastos públicos com Pesquisa e Desenvolvimento - IBGE", "Ano", "(Em Porcentagem do PIB)", "grafico_pesquisa.png")
        imagens.append("/static/data/grafico_pesquisa.png")
        
        # Gráfico 5: PIB per capita
        dados_pib_per_capita = dados[5]['series'][0]['serie']
        pib_per_capita = [(int(k), float(v)) for d in dados_pib_per_capita for k, v in d.items() if v and k != "-"]
        df2 = pd.DataFrame(pib_per_capita)
        plotar_grafico(df2[0], df2[1], "PIB per capita - IBGE", "Ano", "(Em Mil US$)", "grafico_pib_per_capita.png")
        imagens.append("/static/data/grafico_pib_per_capita.png")
        
        # Gráfico 6: Total de Exportações
        dados_exportacoes = dados[7]['series'][0]['serie']
        exportacoes = [(int(k), float(v)) for d in dados_exportacoes for k, v in d.items() if v and k != "-"]
        df2 = pd.DataFrame(exportacoes)
        plotar_grafico(df2[0], df2[1], "Total de Exportações - IBGE", "Ano", "(em Bilhões de US$)", "grafico_exportacoes.png")
        imagens.append("/static/data/grafico_exportacoes.png")
        
        # Gráfico 7: Total de Importações
        dados_importacoes = dados[8]['series'][0]['serie']
        importacoes = [(int(k), float(v)) for d in dados_importacoes for k, v in d.items() if v and k != "-"]
        df2 = pd.DataFrame(importacoes)
        plotar_grafico(df2[0], df2[1], "Total de Importações - IBGE", "Ano", "(em Bilhões de US$)", "grafico_importacoes.png")
        imagens.append("/static/data/grafico_importacoes.png")
        
        # Gráfico 7: Total do Pib
        dados_pib = dados[9]['series'][0]['serie']
        pib = [(int(k), float(v)) for d in dados_pib for k, v in d.items() if v and k != "-"]
        df2 = pd.DataFrame(pib)
        plotar_grafico(df2[0], df2[1], "Total do PIB - IBGE", "Ano", "(em Trilhões de US$)", "grafico_pib.png")
        imagens.append("/static/data/grafico_pib.png")

    except Exception as e:
        print(f"[ERRO] Falha ao processar dados: {e}")
        return template('index', titulo="Erro", imagens=[])

    return template('index', titulo="Indicadores Econômicos - Brasil - IBGE", imagens=imagens)
