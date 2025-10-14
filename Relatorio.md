
---

## 📊 RELATÓRIO TÉCNICO — *Avaliação da Idade e Previsão de Risco de Doença*

```markdown
# 🧪 Relatório Técnico
## Avaliação da Idade e Previsão de Risco de Doença

### 1. Introdução

Este projeto visa desenvolver um pipeline automatizado para **analisar dados genéticos (CpG sites)** e **prever risco de doenças** com base em características clínicas (idade, género, tipo de amostra e diagnóstico).  
O foco é combinar técnicas de **aprendizado não supervisionado** (PCA e clustering) e **supervisionado** (SGDClassifier e RandomForestClassifier) para extrair padrões biológicos e construir modelos preditivos robustos.

---

### 2. Metodologia

#### 2.1. Estrutura de Dados
- **trainmap.csv**: metadados clínicos (idade, género, tipo, doença)
- **traindata.csv**: intensidades genéticas (CpG sites)

#### 2.2. Pré-processamento
- Conversão de formato *wide → long* para permitir fusão entre CpG sites e amostras.
- Integração com `trainmap.csv` via `sample_id`.
- Exportação incremental em ficheiros `.parquet` (otimização de memória).

#### 2.3. Redução de Dimensionalidade e Clustering
- Aplicação de **Incremental PCA** com 2 componentes principais (PC1, PC2).
- Agrupamento com **MiniBatchKMeans** em 4 clusters.
- Geração do dataset `train_processed.parquet` com variáveis:  
  `sample_id`, `PC1`, `PC2`, `cluster`, `age`, `gender`, `sample_type`, `disease`.

#### 2.4. Modelagem Supervisionada
Foram testados dois modelos:
1. **SGDClassifier (log_loss)** — incremental e eficiente para grandes volumes.  
2. **RandomForestClassifier** — modelo ensemble com maior poder de generalização.

#### 2.5. Avaliação
- Métricas: *accuracy*, *precision*, *recall*, *f1-score*.
- Visualização: matrizes de confusão e gráficos interativos.
- Comparação direta entre modelos (SGD vs Random Forest).

#### 2.6. Visualização e Dashboard
- Construído com **Plotly** e **Streamlit** para explorar:
  - Distribuição PCA por género e idade
  - Clusters e prevalência de doenças
  - Correlação entre variáveis clínicas

---

### 3. Resultados Principais

| Modelo | Acurácia | Observações |
|---------|-----------|-------------|
| **SGDClassifier** | Moderada | Aprendeu padrões principais, mas sensível a classes desbalanceadas |
| **RandomForestClassifier** | Alta (em classes majoritárias) | Tende a prever a classe dominante; necessita balanceamento |

- Clusters mostraram correlação com faixa etária e tipo de amostra.
- A PCA reduziu a dimensionalidade mantendo variância explicada relevante (~85% com 2 componentes).
- A matriz de confusão indicou confusão entre doenças com padrões genéticos semelhantes.

---

### 4. Discussão

- **Vantagens da abordagem incremental**: processamento eficiente sem sobrecarregar a RAM.
- **Limitações**: falta de normalização e desbalanceamento de classes afetaram a robustez do modelo.
- **Oportunidades**:
  - Melhorar o pipeline de treino com normalização incremental e balanceamento.
  - Introduzir técnicas de interpretabilidade (SHAP) para identificar CpG sites relevantes.

---

### 5. Conclusões

O pipeline desenvolvido permite:
- Processar dados genéticos em larga escala;
- Reduzir dimensionalidade e identificar padrões clínicos;
- Treinar modelos supervisionados para previsão de risco de doenças;
- Visualizar resultados interativamente via dashboard.




---

📍 **Autor:** André Jorge  
📘 **Disciplina:** Programação Avançada com Python (10794)  
🏫 **Instituição:** Cinel 
📅 **Ano:** 2025


