import pandas as pd

df = pd.read_excel('dados/FILA EXAMES 2024.xlsx')



df['Data do envio'] = pd.to_datetime(df['Data do envio'], format= '%Y-%m-%d %H:%M:%S')

df['Posição na fila'] = df['Posição na fila'].astype(str)
df['Nº Solicitação'] = df['Nº Solicitação'].astype(str)
df['Procedimento'] = df['Procedimento'].astype(str)
df['Unidade Solicitante'] = df['Unidade Solicitante'].astype(str)
df['Codigo municipio solicitante'] = df['Codigo municipio solicitante'].astype(str)
df['Idade'] = df['Idade'].astype(int)
df['Prontuario'] = df['Prontuario'].astype(str)
df['CNS'] = df['CNS'].astype(str)
df['CPF'] = df['CPF'].astype(str)
df['Telefones'] = df['Telefones'].astype(str)
df['Quantidade'] = ''








