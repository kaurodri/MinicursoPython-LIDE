import requests

def getIPCA():
    """
    433: IPCA Inflação oficial do Brasil (meta do BC)
    """

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"
    
    response = requests.get(url)
    dados = response.json()

    result = float(dados[-1]['valor'])

    return result

#print(getIPCA())
