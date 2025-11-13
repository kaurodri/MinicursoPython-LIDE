import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

def criar_tabela_financeira():
  valor_inicial = 1000
  valor_infla = 950
  valor_rendi = 1200
  
  dados = {
    'valor': [valor_inicial],
    'infla': [valor_infla],
    'rendi': [valor_rendi]
  }

  df = pd.DataFrame(dados)
    
  #print("-" * 50)
  #print(df.to_string(index=False))

  #print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

  return df

def plotar_grafico_simples(df):
  valor_inicial = df['valor'].iloc[0]
  valor_infla = df['infla'].iloc[0]
  valor_rendi = df['rendi'].iloc[0]
  
  dias = range(31)
  inflacao = [valor_inicial + ((valor_infla - valor_inicial) / 30) * i for i in dias]
  rendimento = [valor_inicial + ((valor_rendi - valor_inicial) / 30) * i for i in dias]

  plt.plot(dias, inflacao, 'r-', label='Valor com Inflação')
  plt.plot(dias, rendimento, 'g-', label='Valor com Rendimento')
  plt.legend()
  plt.show()

if __name__ == "__main__":
  plotar_grafico_simples(criar_tabela_financeira())