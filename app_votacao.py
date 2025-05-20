import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv("data/votacao_simulada.csv")

# Título
st.title("Análise Interativa da Votação Estudantil")

# Filtros
st.sidebar.header("Filtros")

sexo_opcao = st.sidebar.multiselect("Sexo", options=df["sexo"].unique(), default=df["sexo"].unique())
serie_opcao = st.sidebar.multiselect("Série", options=df["serie"].unique(), default=df["serie"].unique())
chapa_opcao = st.sidebar.multiselect("Chapa Votada", options=df["chapa_votada"].unique(), default=df["chapa_votada"].unique())

# Aplica os filtros
df_filtrado = df[
    (df["sexo"].isin(sexo_opcao)) &
    (df["serie"].isin(serie_opcao)) &
    (df["chapa_votada"].isin(chapa_opcao))
]

st.subheader("Resumo dos Dados Filtrados")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Votantes", len(df_filtrado))
col2.metric("Idade Média", round(df_filtrado["idade"].mean(), 1))
col3.metric("Séries Envolvidas", df_filtrado["serie"].nunique())

# Gráfico 1: Distribuição por sexo
st.subheader("Distribuição por Sexo")
fig1, ax1 = plt.subplots()
sns.countplot(data=df_filtrado, x="sexo", ax=ax1)
st.pyplot(fig1)

# Gráfico 2: Votos por chapa
st.subheader("Votos por Chapa")
fig2, ax2 = plt.subplots()
sns.countplot(data=df_filtrado, x="chapa_votada", ax=ax2)
st.pyplot(fig2)

# Gráfico 3: Distribuição por série
st.subheader("Distribuição por Série Escolar")
fig3, ax3 = plt.subplots()
sns.countplot(data=df_filtrado, x="serie", ax=ax3, order=["1º Ano", "2º Ano", "3º Ano"])
st.pyplot(fig3)

# Gráfico 4: Distribuição etária
st.subheader("Distribuição de Idade")
fig4, ax4 = plt.subplots()
sns.histplot(df_filtrado["idade"], bins=10, kde=True, ax=ax4)
st.pyplot(fig4)
