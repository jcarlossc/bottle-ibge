import requests

def get_indicadores():
    """
    Faz uma requisição à API do IBGE para obter os indicadores para o Brasil.

    Returns:
        Retorna uma lista de dicionários contendo os indicadores, 
        caso a requisição seja bem-sucedida (HTTP 200).
        Retorna None em caso de erro na requisição ou exceção durante a execução.
        
    Observações:
        - A URL acessada é: https://servicodados.ibge.gov.br/api/v1/paises/BR/indicadores
        - É necessário ter a biblioteca `requests` instalada.
    """
    url = "https://servicodados.ibge.gov.br/api/v1/paises/BR/indicadores"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"ERRO - Falha na requisição: {e}")
        return None