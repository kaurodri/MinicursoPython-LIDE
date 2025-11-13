def infla_mensal(valor, ipca_atual):
    resultado = valor * (1 - (1 / (1 + ipca_atual)))
    return resultado