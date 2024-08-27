import pandas as pd
import xlrd
df = pd.read_excel('dados/filademandareprimidaservico26_08_2024.xlsx')



df = df.rename(columns={'numero_fila_espera_geral' : 'Posição na fila'})
df = df.rename(columns={'amb_solicitacao_procedimento_servico_id' : 'Nº Solicitação'})
df = df.rename(columns={'codigo_procedimento' : 'Procedimento'})
df = df.rename(columns={'nome_procedimento' : 'Nome procedimento'})
df = df.rename(columns={'data_hora_envio' : 'Data do envio'})
df = df.rename(columns={'codigo_unidade_solicitacao' : 'Codigo unidade solicitante'})
df = df.rename(columns={'nome_unidade_solicitacao' : 'Unidade solicitante'})
df = df.rename(columns={'codigo_municipio_solicitante' : 'Codigo municipio solicitante'})
df = df.rename(columns={'nome_municipio_solicitante' : 'Nome municipio solicitante'})
df = df.rename(columns={'idade' : 'Idade'})
df = df.rename(columns={'nivel_prioridade' : 'Prioridade'})
df = df.rename(columns={'numprontuario_paciente' : 'Prontuario'})
df = df.rename(columns={'data_nascimento_paciente' : 'Data de nascimento'})
df = df.rename(columns={'numero_cartao_paciente' : 'CNS'})
df = df.rename(columns={'numero_cpf_paciente' : 'CPF'})
df = df.rename(columns={'nome_paciente' : 'Nome do paciente'})
df = df.rename(columns={'nome_mae' : 'Nome da mae'})
df = df.rename(columns={'lista_telefones' : 'Telefones'})
df = df.rename(columns={'codigo_municipio_residencia' : 'Municipio de residencia'})

df['Nº Solicitação'] = df['Nº Solicitação'].astype(str)
df['Procedimento'] = df['Procedimento'].astype(str)
df['Codigo unidade solicitante'] = df['Codigo unidade solicitante'].astype(str)
df['Codigo municipio solicitante'] = df['Codigo municipio solicitante'].astype(str)
df['Idade'] = df['Idade'].astype(int)
df['Prontuario'] = df['Prontuario'].astype(str)
df['CNS'] = df['CNS'].astype(str)
df['CPF'] = df['CPF'].astype(str)
df['Telefones'] = df['Telefones'].astype(str)
df['Quantidade'] = ''
df['Data do envio'] = pd.to_datetime(df['Data do envio'], format='%d/%m/%Y')
        










