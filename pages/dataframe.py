import streamlit as st
from dataset_exames import df
from utils import convert_csv, mensagem_sucesso



st.title('Fila de espera Pouso Alegre :calendar:')


with st.expander('Colunas'):
    Colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),
        list(df.columns)
    )

st.sidebar.title('Filtros')
with st.sidebar.expander('Nome procedimento'):
    
    all_options = st.checkbox("Selecione todos os procedimentos")
    if all_options:
        procedimentos = st.multiselect(
        'Selecione o procedimento',
        df['Nome procedimento'].unique(),
        df['Nome procedimento'].unique(),
        placeholder='Procedimento',
    )
    else:
        procedimentos = st.multiselect(
        'Selecione o procedimento',
        df['Nome procedimento'].unique(),
        

        placeholder='Procedimento',
        )





with st.sidebar.expander('Data do envio'):
    data_do_envio = st.date_input(
        'Selecione a data do envio',
        (df['Data do envio'].min(),
        df['Data do envio'].max()
        ),
        format="DD.MM.YYYY",
        
    )

with st.sidebar.expander('Idade'):
    idade = st.slider(
        'Selecione a idade',
        0, 130,
        (0, 130),
        )


query = '''
    `Nome procedimento` in @procedimentos and \
    @idade[0] <= Idade <= @idade[1] and \
    @data_do_envio[0] <= `Data do envio` <= @data_do_envio[1]
'''

filtro_dados = df.query(query)
filtro_dados = filtro_dados[Colunas]


st.markdown(f'Quantidade de pacientes :blue[{filtro_dados.shape[0]}]')

st.markdown('Nome do arquivo')

coluna1, coluna2 = st.columns(2)

with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility='collapsed'
    )
    nome_arquivo += '.csv'

with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso
    )
st.dataframe(filtro_dados)


