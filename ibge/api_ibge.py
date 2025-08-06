import requests

def get_indicadores():
    url = "https://servicodados.ibge.gov.br/api/v1/paises/BR/indicadores"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"ERRO - Falha na requisição: {e}")
        return None