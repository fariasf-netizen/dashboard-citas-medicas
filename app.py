import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('citas_medicas.csv')

st.title('Dashboard de Gestión de Citas Médicas')

# Gráfico 1: Citas por Especialidad
st.subheader('Citas por Especialidad')
conteo_esp = df['especialidad'].value_counts().reset_index()
conteo_esp.columns = ['Especialidad', 'Cantidad']
fig1 = px.bar(conteo_esp, x='Especialidad', y='Cantidad')
st.plotly_chart(fig1)

# Gráfico 2: Estado de las Citas
st.subheader('Estado de las Citas')
fig2 = px.pie(df, names='estado')
st.plotly_chart(fig2)

# Gráfico 3: Citas por Mes
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month
citas_mes = df.groupby('mes').size().reset_index(name='cantidad')

st.subheader('Citas por Mes')
fig3 = px.line(citas_mes, x='mes', y='cantidad', markers=True)
st.plotly_chart(fig3)
