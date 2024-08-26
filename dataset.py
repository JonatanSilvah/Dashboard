import pandas as pd

df = pd.read_excel('dados/Consultas 2024.xlsx')

df['data_agenda'] = pd.to_datetime(df['data_agenda'], format= '%d/%m/%Y')

df['data_recepcao'] = pd.to_datetime(df['data_recepcao'], format= '%d/%m/%Y')

df['data_realizacao_agendamento'] = pd.to_datetime(df['data_realizacao_agendamento'], format= '%d/%m/%Y')

df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], format= '%d/%m/%Y')

df['data_solicitacao'] = pd.to_datetime(df['data_solicitacao'], format= '%d/%m/%Y')

df['codigo_solicitacao'] = df['codigo_solicitacao'].astype(str)
df['codigo_unidade_solicitacao'] = df['codigo_unidade_solicitacao'].astype(str)
df['codigo_especialidade_solicitacao'] = df['codigo_especialidade_solicitacao'].astype(str)
df['codigo_profissional_solicitacao'] = df['codigo_profissional_solicitacao'].astype(str)
df['numero_prontuario'] = df['numero_prontuario'].astype(str)
df['Idade'] = df['Idade'].astype(str)
df['cpf'] = df['cpf'].astype(str)
df['cns'] = df['cns'].astype(str)
df['codigo_municipio_residencia'] = df['codigo_municipio_residencia'].astype(str)
df['numimovel'] = df['numimovel'].astype(str)
df['cep'] = df['cep'].astype(str)
df['telcontato'] = df['telcontato'].astype(str)
df['codigo_procedimento'] = df['codigo_procedimento'].astype(str)
df['codigo_cbo_executante'] = df['codigo_cbo_executante'].astype(str)
df['codigo_especialidade_cbo_executante'] = df['codigo_especialidade_cbo_executante'].astype(str)
df['codigo_municipio_agenda'] = df['codigo_municipio_agenda'].astype(str)
df['codigo_unidade_agenda'] = df['codigo_unidade_agenda'].astype(str)
df['codigo_profissional_agenda'] = df['codigo_profissional_agenda'].astype(str)
df['codigo_especialidade_agenda'] = df['codigo_especialidade_agenda'].astype(str)


