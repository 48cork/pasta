import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Monitor de Tensões UFCG", layout="wide")

st.title("📊 Monitor de Tensões Sociológicas - UACS/UFCG")
st.markdown("""
Este painel visualiza os dados coletados pelo **Squad de IAs** (Marx, Weber, Durkheim e Bourdieu) 
sobre a realidade dos estudantes.
""")

# Carregar os dados que criamos na Aula 6
df = pd.read_csv("matriz_diagnostica_ufcg.csv")

# Layout de Colunas
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição por Teoria Dominante")
    fig_pie = px.pie(df, names='teoria_dominante', title="Quais autores explicam a crise atual?", hole=0.3)
    st.plotly_chart(fig_pie)

with col2:
    st.subheader("Intensidade das Tensões")
    fig_bar = px.bar(df, x='id_aluno', y='intensidade', color='teoria_dominante', 
                     hover_data=['conceito_chave'], title="Nível de Impacto por Aluno")
    st.plotly_chart(fig_bar)

st.subheader("📋 Base de Dados Bruta")
st.dataframe(df)

st.sidebar.info(f"Total de Relatos Processados: {len(df)}")
