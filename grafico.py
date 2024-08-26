
from utils import df_procedimentos
import plotly.express as px 

grafico_procedimentos = px.bar(
    df_procedimentos.sort_values('Quantidade', ascending=False).head(10),
    x = 'Quantidade',
    y = 'Nome procedimento',
    text_auto = True,
    title = '10 exames mais solicitados'
)