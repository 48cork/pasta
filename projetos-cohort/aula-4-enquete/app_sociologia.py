import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sociologia de Dados - UFCG", layout="wide")

st.title("🏛️ Sociologia de Dados: Observatório de Tensões (UACS/UFCG)")
st.markdown("---")

# Carregar Dados
df = pd.read_csv("matriz_diagnostica_ufcg.csv")

# Métricas no Topo
m1, m2, m3 = st.columns(3)
m1.metric("Relatos Processados", len(df))
m2.metric("Tensão Média", round(df['intensidade'].mean(), 1))
m3.metric("Alerta Vermelho (I=5)", len(df[df['intensidade'] == 5]))

st.markdown("---")

# Colunas de Gráficos
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("Frequência Teórica")
    fig_pie = px.pie(df, names='teoria_dominante', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Distribuição de Impacto por Aluno")
    fig_bar = px.bar(df, x='id_aluno', y='intensidade', color='teoria_dominante',
                     text='conceito_chave', barmode='group')
    st.plotly_chart(fig_bar, use_container_width=True)

# SEÇÃO DE INSIGHTS (A Inteligência da Aula 9)
st.markdown("---")
st.subheader("🧠 Insights Estratégicos do Observatório")

c1, c2 = st.columns(2)

with c1:
    dominate = df['teoria_dominante'].mode()[0]
    st.info(f"**Teoria Dominante:** A lente de **{dominate}** é a que melhor explica o mal-estar atual da amostra.")
    
with c2:
    high_risk = df[df['intensidade'] == 5]['id_aluno'].tolist()
    if high_risk:
        st.error(f"**Atenção Crítica:** Os alunos {high_risk} apresentam sinais de ruptura iminente (Intensidade 5).")
    else:
        st.success("Nenhum caso de ruptura máxima detectado no momento.")

st.subheader("📋 Base de Dados Completa")
st.dataframe(df, use_container_width=True)

st.sidebar.markdown("### 🛠️ Filtro de Análise")
teoria_filter = st.sidebar.multiselect("Filtrar por Teoria:", options=df['teoria_dominante'].unique(), default=df['teoria_dominante'].unique())
df_filtered = df[df['teoria_dominante'].isin(teoria_filter)]
# (Opcional: vincular os gráficos ao df_filtered para torná-lo dinâmico)

# --- FUNÇÃO DE EXPORTAÇÃO (AULA 10) ---
st.markdown("---")
st.subheader("📤 Exportar Evidências")

@st.cache_data
def convert_df(df_to_convert):
    return df_to_convert.to_csv(index=False).encode('utf-8')

csv_data = convert_df(df_filtered)

st.download_button(
    label="📥 Baixar Matriz de Dados (CSV)",
    data=csv_data,
    file_name='relatorio_sociologia_dados_ufcg.csv',
    mime='text/csv',
)

st.success("Relatório pronto para exportação institucional.")
