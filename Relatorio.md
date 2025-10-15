📊 RELATÓRIO TÉCNICO — Avaliação da Idade e Previsão de Risco de Doença

1-Introdução

  Este projeto visa desenvolver um pipeline automatizado para analisar dados genéticos (CpG sites) e prever risco de doenças com base em características clínicas (idade, género, tipo de amostra e diagnóstico).
  O foco é combinar técnicas de aprendizado não supervisionado (PCA e clustering) e supervisionado (SGDClassifier e RandomForestClassifier) para extrair padrões biológicos e construir modelos preditivos robustos.

📦 Fonte dos Dados:
  Os datasets utilizados foram obtidos na plataforma Kaggle, disponíveis em:
  
  🔗 Age Assessment and Disease Risk Prediction 
  (https://www.kaggle.com/datasets/marquis03/age-assessment-and-disease-risk-prediction)

2.Metodologia

  2.1. Estrutura de Dados

   - trainmap.csv: metadados clínicos (idade, género, tipo, doença)
   - traindata.csv: intensidades genéticas (CpG sites)

  2.2. Pré-processamento

  - Conversão de formato wide → long para permitir fusão entre CpG sites e amostras.
  - Integração com trainmap.csv via sample_id.
  - Exportação incremental em ficheiros .parquet para otimização de memória.

  2.3. Redução de Dimensionalidade e Clustering

  - Aplicação de Incremental PCA com 2 componentes principais (PC1, PC2).
  - Agrupamento com MiniBatchKMeans em 4 clusters.
  - Geração do dataset train_processed.parquet com variáveis:
        sample_id, PC1, PC2, cluster, age, gender, sample_type, disease.

  2.4. Modelagem Supervisionada

  Foram testados dois modelos:

  1- SGDClassifier (log_loss) — incremental e eficiente para grandes volumes.
  2- RandomForestClassifier — ensemble de árvores com maior poder de generalização.

  2.5. Avaliação

  - Métricas: accuracy, precision, recall, f1-score.
  - Visualização: matrizes de confusão e gráficos interativos.
  - Comparação direta entre modelos (SGD vs Random Forest).

2.6. Visualização e Dashboard

  Construído com Plotly e Streamlit, permitindo explorar:

  - Distribuição PCA por género e idade
  - Clusters e prevalência de doenças
  - Correlação entre variáveis clínicas

3.Resultados Principais
   
  3.1. Resultados do PCA e Clustering

  O Incremental PCA foi treinado com sucesso, retendo cerca de 85% da variância total nas duas primeiras componentes.
  O resultado foi salvo em:
  - train_processed.parquet


Exemplo das amostras:

| Sample_id	|    PC1	  |   PC2	   |   Cluster	|   Age	 |     Gender	   |   Sample_type	      |        Disease        |
| --------- | --------- | -------- | ---------- | ------ | ------------- | -------------------- | --------------------- |
|   0	      |   414.55	|   45.47	 |      1	    |    88	 |       F	     |  disease tissue	    |   Alzheimer's disease |
|   1	      |  -148.82	|    9.91	 |      2	    |    92	 |       F	     |  disease tissue	    |   Alzheimer's disease |
|   2	      |  -211.14	|   -1.67	 |      3     |  	 93  |       F	     |  disease tissue	    |   Alzheimer's disease |
|   3       |    327.86 |   -12.7  |      3     |    96  |       F       |  disease tissue      |   Alzheimer's disease |
|   4       |   -24.99  |   -6.7   |      2     |    91  |       M       |  disease tissue      |   Alzheimer's disease |

📊 Distribuição de amostras por cluster:

| Cluster | Nº de amostras |
| ------- | -------------- |
|    0    |      510       |
|    1    |     1180       |
|    2    |      656       |
|    3    |     1168       |


Análise:

 - Os clusters apresentaram tendência de agrupamento por faixa etária e tipo de amostra, o que indica que o PCA conseguiu separar parcialmente padrões biológicos relevantes.
 - O Cluster 1 foi o mais representativo, sugerindo uma predominância de amostras com características genéticas semelhantes (possivelmente associadas a um grupo etário ou diagnóstico dominante).
 - A visualização PCA mostrou sobreposição parcial entre doenças neurodegenerativas, evidenciando proximidade genética entre Alzheimer, Parkinson e esquizofrenia.

3.2. Resultados dos Modelos Supervisionados

📊 SGDClassifier (Log Loss)

|        Métrica        | Valor |
| --------------------- | ----- |
| **Accuracy**          |  0.32 |
| **Macro F1-score**    |  0.07 |
| **Weighted F1-score** |  0.40 |


  Resumo:

  O modelo conseguiu identificar parcialmente padrões da classe control, com precision e recall moderados (0.76 e 0.38).
  Demais doenças apresentaram recall próximo de 0, indicando grande desbalanceamento e dificuldade em generalizar.
  Apesar disso, o SGD apresentou comportamento coerente com sua natureza incremental e sensibilidade a classes minoritárias.

🌲 RandomForestClassifier

|        Métrica        | Valor |
| --------------------- | ----- |
| **Accuracy**          | 1.00  |
| **Macro F1-score**    | 1.00  |
| **Weighted F1-score** | 1.00  |


  Resumo:

  O modelo obteve performance perfeita em treino — um claro indício de overfitting.
  É provável que o modelo tenha memorizado os dados de treino (sem divisão treino/teste adequada ou sem validação cruzada).
  Apesar da alta performance aparente, é necessário introduzir técnicas de validação externa, balanceamento de classes e feature scaling para garantir robustez.

4.Discussão

 - Incremental PCA demonstrou excelente eficiência computacional, permitindo processar dados de larga escala sem sobrecarregar a RAM.

 - O clustering revelou padrões clínicos e genéticos, mas requer análise mais aprofundada para interpretar associações entre grupos e doenças.

 - O SGDClassifier teve desempenho modesto, refletindo sensibilidade ao desbalanceamento e à ausência de normalização.

 - O RandomForestClassifier, embora mostre acurácia perfeita, não é confiável sem validação externa — há forte indício de overfitting.

 - 

  📈 Oportunidades de melhoria:

  - Normalização incremental das features.
  - Aplicação de stratified sampling para divisão treino/teste.
  - Balanceamento de classes via SMOTE ou class_weight='balanced'.
  - Uso de métricas adicionais (AUC, ROC) e interpretabilidade (SHAP, feature importance).

5.Conclusões

  O pipeline desenvolvido permite:
  - Processar dados genéticos em larga escala com eficiência incremental;
  - Reduzir dimensionalidade e identificar padrões clínicos via PCA + KMeans;
  - Treinar modelos supervisionados para previsão de risco de doenças;
  - Visualizar resultados interativamente num dashboard Streamlit.
  - Apesar dos bons resultados visuais, o desempenho supervisionado requer melhorias de generalização e balanceamento antes de uso em cenários reais.






📍 Autor: André Jorge

📘 Disciplina: Programação Avançada com Python (10794)

🏫 Instituição: Cinel

📅 Ano: 2025








