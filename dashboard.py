import os
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ===== CONFIGURAÇÃO =====
SRC_DIR = r"C:\Users\andr3\Documents\DATA SCIENCE\10794 - Programação avançada com Python\Age Assessment & Disease Risk Prediction\src"
CLEAN_FOLDER = os.path.join(SRC_DIR, "clean")
PARQUET_FILE = os.path.join(CLEAN_FOLDER, "train_processed.parquet")

# ===== CARREGAR DADOS =====
@st.cache_data
def carregar_dados():
    return pd.read_parquet(PARQUET_FILE)

if not os.path.exists(PARQUET_FILE):
    st.error(f"Nenhum arquivo encontrado em {PARQUET_FILE}")
    st.stop()

df = carregar_dados()

# ===== SIDEBAR FILTROS =====
st.sidebar.header("Filtros")
idade = st.sidebar.slider("Idade", int(df["age"].min()), int(df["age"].max()), (20, 60))
genero = st.sidebar.multiselect("Gênero", options=df["gender"].dropna().unique(),
                                default=list(df["gender"].dropna().unique()))
tipo = st.sidebar.multiselect("Tipo de amostra", options=df["sample_type"].dropna().unique(),
                              default=list(df["sample_type"].dropna().unique()))
doenca = st.sidebar.multiselect("Doença", options=df["disease"].dropna().unique(),
                                default=list(df["disease"].dropna().unique()))

# ===== APLICAR FILTROS =====
df_filtrado = df[
    (df["age"].between(idade[0], idade[1])) &
    (df["gender"].isin(genero)) &
    (df["sample_type"].isin(tipo)) &
    (df["disease"].isin(doenca))
]

if df_filtrado.empty:
    st.warning("Nenhum dado corresponde aos filtros selecionados.")
    st.stop()

# ===== DASHBOARD =====
st.title("🧬 Dashboard de Clusters - Avaliação Biológica")
st.metric("Amostras selecionadas", len(df_filtrado))

fig_pca = px.scatter(df_filtrado, x="PC1", y="PC2", color="cluster",
                     hover_data=["sample_id", "age", "gender", "sample_type", "disease"],
                     title="Clusters no Espaço PCA")
st.plotly_chart(fig_pca, use_container_width=True)

fig_gender = px.scatter(df_filtrado, x="PC1", y="PC2", color="gender", symbol="cluster",
                        hover_data=["sample_id", "age", "sample_type", "disease"],
                        title="Distribuição PCA por Gênero")
st.plotly_chart(fig_gender, use_container_width=True)

doenca_cluster = df_filtrado.groupby(["cluster", "disease"]).size().reset_index(name="n")
fig_doenca = px.bar(doenca_cluster, x="cluster", y="n", color="disease",
                    title="Distribuição de Doenças por Cluster", barmode="stack")
st.plotly_chart(fig_doenca, use_container_width=True)

fig_box = px.box(df_filtrado, x="cluster", y="age", color="cluster",
                 title="Distribuição de Idade por Cluster")
st.plotly_chart(fig_box, use_container_width=True)

with st.expander("🔍 Ver correlações"):
    df_corr = df_filtrado.copy()
    for col in ["gender", "sample_type", "disease"]:
        df_corr[col] = df_corr[col].astype("category").cat.codes
    corr_matrix = df_corr[["age", "gender", "sample_type", "disease", "cluster"]].corr()
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

count_df = df_filtrado["cluster"].value_counts().rename("n_amostras").reset_index().rename(columns={"index": "cluster"})
st.subheader("📊 Contagem por Cluster")
st.dataframe(count_df)

st.download_button("📥 Baixar dados filtrados", df_filtrado.to_csv(index=False), "dados_filtrados.csv")
