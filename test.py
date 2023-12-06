import pandas as pd

url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

dados_co2 = pd.read_excel(url)
dados_co2.head()

pd.ExcelFile(url).sheet_names

percapita = pd.read_excel(url, sheet_name='emissoes_percapita')
percapita.head()

percapita = pd.read_excel(url, sheet_name='fontes')
percapita.head()

intervalo = pd.read_excel(url, sheet_name='emissoes_co2', usecols='A:D')
intervalo
intervalo.head()
