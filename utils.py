import pandas as pd
from dataset_exames import df
import streamlit as st
import time
df_total = df
df_total['Quantidade'] = df.groupby('Procedimento')['Procedimento'].transform('count')
df_procedimentos = df_total.drop_duplicates(subset='Procedimento')[['Nome procedimento', 'Quantidade']]



@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')


def mensagem_sucesso():
    success = st.success(
        'baixado com sucesso',
    )
    time.sleep(3)
    success.empty()