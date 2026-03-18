import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sociologia de Dados - UFCG", layout="wide")

# Título Oficial do Projeto
st.title("🏛️ Sociologia de Dados: Observatório de Tensões (UACS/UFCG)")
st.markdown("---")

# Carregar Dados
df = pd.read_csv("matriz_diagnostica_ufcg.csv")

# Cálculo de Métricas Rápidas
total_relatos = len(df)
crise_maxima = len(df[df['intensidade'] == 5])

# Exibir "Big Numbers" no topo
m1, m2, m3 = st.columns(3)
m1.metric("Total de Relatos", total_relatos)
m2.metric("Nível de Tensão Médio", round(df['intensidade'].mean(), 1))
m3.metric("Casos em Crise Máxima", crise_maxima, delta_color="inverse")

st.markdown("---")

# Layout de Colunas para Gráficos
col1, col2 = st.columns(2)

with col1:
    st.subheader("Frequência Teórica")
    fig_pie = px.pie(df, names='teoria_dominante', hole=0.4, 
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie)

with col2:
    st.subheader("Mapa de Calor da Intensidade")
    fig_bar = px.bar(df, x='id_aluno', y='intensidade', color='teoria_dominante',
                     hover_data=['conceito_chave'], barmode='group')
    st.plotly_chart(fig_bar)

st.subheader("📋 Base de Dados Estruturada")
st.dataframe(df, use_container_width=True)

st.sidebar.header("Sobre o Projeto")
st.sidebar.info("Desenvolvido pelo Prof. Sergio Farias como ferramenta de diagnóstico sociológico digital.")
