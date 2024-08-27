import streamlit as st
import plotly.express as px 
from dataset_exames import df
#from grafico import grafico_procedimentos
import pandas as pd
from utils import df_procedimentos




st.set_page_config(layout='wide')

st.title('Fila de espera de exames especializados Pouso Alegre')
st.text('Última atualização 26/08/2024\nDados confidenciais' )


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
    colum1, colum2 = st.columns(2)
    with colum1:
        st.metric('Total de pacientes na fila de espera', df_procedimentos['Quantidade'].sum())
    with colum2:
        st.title('Total por procedimento')
        st.dataframe(df_procedimentos.sort_values('Quantidade', ascending=False))



