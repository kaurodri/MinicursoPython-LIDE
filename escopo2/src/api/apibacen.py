import requests

def getSelic():
    """
    Obtém o valor mais recente da taxa SELIC da API do Banco Central
    
    432: Taxa SELIC acumulada no mês (meta)
    11: Taxa SELIC diária
    1178: Histórico da taxa SELIC anualizada
    """

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json&dataInicial=10/11/2025&dataFinal=11/11/2025"
    
    response = requests.get(url)
    dados = response.json()

    valorRecente = dados[0]['valor']

    return float(valorRecente)
