# 🧬 Age Assessment & Disease Risk Prediction

### 📊 Avaliação da Idade e Previsão de Risco de Doença

Este repositório contém o **pipeline completo para avaliação de idade e predição de risco de doenças** a partir de **dados epigenéticos (CpG sites)**.  
O projeto integra processamento de dados, análise exploratória, redução de dimensionalidade, clustering e modelagem preditiva com **aprendizado supervisionado e não supervisionado**.

---

## ⚙️ Estrutura do Projeto

| Ficheiro | Descrição |
|-----------|------------|
| **preprocessing.py** | Limpeza e transformação incremental dos dados genéticos |
| **train_models.py** | Treino dos modelos de Machine Learning (SGDClassifier e RandomForestClassifier) |
| **dashboard.py** | Dashboard interativo com Plotly + Streamlit |
| **projecto.ipynb** | Análise exploratória, PCA e clustering |
| **Relatorio.md / .pdf** | Relatório técnico detalhado do projeto |

---

## 📦 Fonte dos Dados

Os datasets utilizados foram obtidos na plataforma **Kaggle**:  
🔗 [Age Assessment and Disease Risk Prediction](https://www.kaggle.com/datasets/marquis03/age-assessment-and-disease-risk-prediction)

---

## 🧰 Dependências Principais

Instalação recomendada:
```bash
pip install pandas numpy scikit-learn seaborn matplotlib plotly pyarrow joblib streamlit
```

### Bibliotecas utilizadas
- **pandas**, **numpy** → manipulação e análise de dados  
- **scikit-learn** → PCA, KMeans, SGDClassifier, RandomForestClassifier  
- **plotly**, **matplotlib**, **seaborn** → visualizações  
- **pyarrow** → leitura/escrita eficiente em `.parquet`  
- **streamlit** → dashboard interativo  
- **joblib** → serialização de modelos  

---

## 🚀 Como Executar

### 1️⃣ Pré-processamento dos dados
```bash
python preprocessing.py
```

### 2️⃣ Treinar modelos supervisionados
```bash
python train_models.py
```

### 3️⃣ Visualizar resultados e análises interativas
```bash
python dashboard.py
```

---

## 📈 Resultados Principais

### 🔹 PCA + Clustering
- **Incremental PCA (2 componentes)** → retenção de ~85% da variância  
- **MiniBatchKMeans (4 clusters)** → padrões genéticos e clínicos identificados  

| Cluster | Nº de Amostras |
|----------|----------------|
| 0 | 510 |
| 1 | 1180 |
| 2 | 656 |
| 3 | 1168 |

O **Cluster 1** concentrou a maioria das amostras, indicando perfis genéticos dominantes associados à idade e tipo de tecido.

---

### 🔹 Modelos Supervisionados

| Modelo | Accuracy | F1-score (macro) | Observações |
|---------|-----------|-----------------|--------------|
| **SGDClassifier (log_loss)** | 0.32 | 0.07 | Aprendeu padrões principais, mas sensível a classes desbalanceadas |
| **RandomForestClassifier** | 1.00 | 1.00 | Overfitting evidente — requer validação cruzada |

**Principais visualizações:**
- Distribuição PCA por idade e género  
- Clusters de amostras no espaço PCA  
- Matrizes de confusão e métricas de classificação  
- Prevalência de doenças e correlação entre variáveis clínicas  

---

## 💬 Discussão e Perspectivas

- O **Incremental PCA** foi eficiente e permitiu processar dados de larga escala.  
- O **clustering** revelou padrões genéticos coerentes, mas com sobreposição entre doenças neurodegenerativas.  
- O **SGDClassifier** mostrou desempenho moderado devido ao desbalanceamento de classes.  
- O **RandomForestClassifier** apresentou *overfitting*, indicando necessidade de validação e regularização.  

### 🧩 Melhorias Futuras
- Balanceamento de classes (*SMOTE*, *class_weight*)  
- Normalização incremental de features  
- Avaliação com *ROC-AUC* e validação cruzada  
- Análise de interpretabilidade com **SHAP**  

---

## 🧠 Conclusões

O pipeline permite:
- Processamento eficiente e escalável de dados genéticos  
- Redução de dimensionalidade e descoberta de padrões clínicos  
- Treino e comparação de modelos supervisionados  
- Visualização interativa dos resultados  

Apesar dos bons resultados exploratórios, é necessária melhoria de **generalização** e **robustez** dos modelos.

---

## 🧑‍💻 Autor e Informações

**Autor:** André Jorge  
**Disciplina:** Programação Avançada com Python (10794)  
**Instituição:** Cinel  
**Ano:** 2025  

📘 *Projeto desenvolvido no âmbito da unidade curricular “Programação Avançada com Python (10794)” — Cinel, 2025.*











