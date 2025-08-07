import matplotlib.pyplot as plt

def plotar_grafico(x, y, titulo, xlabel, ylabel, nome_arquivo):
    """
    Gera e salva um gráfico de linha simples a partir de dados fornecidos.

    Parâmetros:
        x (list or array-like): Valores do eixo X (ex: anos, categorias).
        y (list or array-like): Valores do eixo Y (ex: indicadores numéricos).
        titulo (str): Título do gráfico.
        xlabel (str): Rótulo do eixo X.
        ylabel (str): Rótulo do eixo Y.
        nome_arquivo (str): Nome do arquivo para salvar o gráfico (dentro da pasta 'data/').

    Comportamento:
        - Cria um gráfico com tamanho 12x4.
        - Plota os dados com marcadores em cada ponto.
        - Habilita o grid e aplica layout ajustado.
        - Salva o gráfico como imagem (png) no caminho "data/nome_arquivo".
        - Fecha a figura após salvar para liberar memória.

    Requisitos:
        - A pasta "data/" deve existir no diretório do projeto.
        - A biblioteca `matplotlib` deve estar instalada.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='tab:blue')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"data/{nome_arquivo}")
    plt.close()