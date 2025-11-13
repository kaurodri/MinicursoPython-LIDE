def calcular_rendimento_selic(valor_inicial, taxa_selic_anual, dias_uteis):
    """
    Calcula o rendimento do Tesouro Selic
    
    valor_inicial: Valor inicial investido (P)
    taxa_selic_anual: Taxa Selic anual em decimal (ex: 0.1375 para 13,75%)
    dias_uteis: Número de dias úteis do investimento (t)
    
    Retorna:
    float: Rendimento calculado
    """
    rendimento = valor_inicial * ((1 + taxa_selic_anual) ** (dias_uteis / 252) - 1)
    return rendimento

#print(calcular_rendimento_selic(16000, 0.1415, 30))
