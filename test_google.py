import pandas as pd

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

dados_co2_sheets = pd.read_csv(url)
dados_co2_sheets.head()

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
sheet_name = 'emissoes_percapita'
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet=(sheet_name)'

percapita_sheets = pd.read_csv(url_percapita)
percapita_sheets.head()

sheet_id = '1lzq0k-41-MbbS63C3Q9i1wPvLkSJt9zhr4Jolt1vEog'
sheet_name = 'fontes'
url_fontes = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

fontes_sheets = pd.read_csv(url_fontes)
fontes_sheets.head()

# %%