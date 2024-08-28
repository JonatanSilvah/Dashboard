import pandas as pd
df = pd.read_excel('dados/fila_de_espera_att.xlsx')



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
df = df.rename(columns={'nome_municipio_residencia' : 'Municipio de residencia'})

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

df = df.drop("numero_ordem", axis=1)
df = df.drop("lista_numero_fila_espera", axis=1)
df = df.drop("codigo_procedimento_cirurgico", axis=1)
df = df.drop("nome_procedimento_cirurgico", axis=1)
df = df.drop("codigo_cid_justifica_solicitacao", axis=1)
df = df.drop("descricao_cid_justifica_solicitacao", axis=1)
df = df.drop("justificativa_solicitacao", axis=1)
df = df.drop("data_min_agendamento", axis=1)
df = df.drop("observacao", axis=1)
df = df.drop("tipo_atendimento_executante", axis=1)
df = df.drop("codigo_especialidade_executante", axis=1)
df = df.drop("codigo_profissional_executante", axis=1)
df = df.drop("numero_prontuario_grupo", axis=1)
df = df.drop("codigo_municipio_residencia", axis=1)
df = df.drop("codigo_municipio_solicitacao", axis=1)
df = df.drop(" municipio", axis=1)
df = df.drop("unidade", axis=1)
df = df.drop("codigo_unidade_solicitante", axis=1)
df = df.drop("nome_unidade_solicitante", axis=1)
df = df.drop("tipo_atendimento_nome", axis=1)
df = df.drop("servico_tipo_id", axis=1)
df = df.drop("ram_servico_fila_espera_id", axis=1)
df = df.drop("ordem_prioridade", axis=1)
df = df.drop("nome_prioridade", axis=1)
df = df.drop("ram_servico_fila_nivel_prioridade_id", axis=1)
df = df.drop("motivo_removido_id", axis=1)
df = df.drop("motivo_priorizacao_id", axis=1)
df = df.drop("situacao", axis=1)
df = df.drop("operador_alteracao_id", axis=1)
df = df.drop("amb_item_solicitacao_procedimento_servico_id", axis=1)
df = df.drop("codigo_unidade_referencia", axis=1)
df = df.drop("codigo_profissional_solicitante", axis=1)
df = df.drop("nome_profissional_solicitado", axis=1)
df = df.drop("profissional", axis=1)
df = df.drop("codigo_especialidade_solicitante", axis=1)
df = df.drop("nome_especialidade_solicitante", axis=1)
df = df.drop("codigo_especialidade_solicitado", axis=1)
df = df.drop("nome_especialidade_solicitado", axis=1)
df = df.drop("especialidade", axis=1)
df = df.drop("codigo_cbo_especialidade", axis=1)
df = df.drop("cbo_especialidade", axis=1)
df = df.drop("quantidade_solicitada", axis=1)
df = df.drop("procedimento", axis=1)
df = df.drop("data_hora_alteracao", axis=1)
df = df.drop("total", axis=1)
        










