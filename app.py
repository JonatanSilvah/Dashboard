import streamlit as st
import plotly.express as px 

#from grafico import grafico_procedimentos
import pandas as pd
from utils import df_procedimentos


st.set_page_config(page_icon=':calendar:')
st.title('Fila de espera de exames especializados Pouso Alegre')
st.text('Última atualização 28/08/2024\nDados confidenciais' )


st.sidebar.title('Filtro de procedimento')


filtro_procedimento2 = st.sidebar.multiselect(
    'Procedimentos',
    df_procedimentos['Nome procedimento'].unique(),
    placeholder='Escolha o procedimento'
    
)
if filtro_procedimento2:
    df_procedimentos = df_procedimentos[df_procedimentos['Nome procedimento'].isin(filtro_procedimento2)]




grafico_procedimentos = px.bar(
    filtro_procedimento2,
    x = df_procedimentos['Quantidade'],
    y = df_procedimentos['Nome procedimento'],
    text_auto = True,
    color=df_procedimentos['Quantidade'],
    color_continuous_scale='Bluered_r',
    labels={'pop':'population of Canada'}, height=400,
    title = 'Quantidade de solicitações por exame',
    
)
aba1, aba2,  = st.tabs(['Graficos', 'Dados consolidados'])



with aba1:
    st.plotly_chart(grafico_procedimentos)
    
with aba2:
    st.metric('Total de pacientes na fila de espera', df_procedimentos['Quantidade'].sum())
    st.text('Total de pacientes por procedimento')
    st.data_editor(
        df_procedimentos.sort_values('Quantidade', ascending=False),
    )