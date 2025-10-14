# Relatório do Projeto: Age Assessment & Disease Risk Prediction

## Objetivo

O projeto tem como objetivo analisar dados epigenéticos para prever a idade e o risco de determinadas doenças, utilizando técnicas de PCA, clustering e modelos supervisionados.

## Metodologia

1. **Pré-processamento**
   - Leitura de arquivos CSV.
   - Transformação wide → long.
   - Merge com informações adicionais (`trainmap.csv`).
   - Exportação em Parquet para facilitar processamento incremental.

2. **Redução de Dimensionalidade**
   - Incremental PCA (2 componentes).
   - Visualização de clusters no espaço PCA.

3. **Clustering**
   - MiniBatch KMeans com 4 clusters.
   - Análise de distribuição de idade, gênero e doenças por cluster.

4. **Modelos Supervisionados**
   - SGDClassifier (mini-batches, loss log-loss).
   - RandomForestClassifier (100 árvores).
   - Avaliação por classification report e matriz de confusão.

5. **Visualização**
   - Gráficos interativos com Plotly.
   - Heatmaps de correlação com Seaborn.
   - Dashboards opcionais (`dashboard.py`).

## Resultados

- Visualização clara de clusters no espaço PCA.
- Previsão de doenças com precisão satisfatória (ver classification reports).
- Identificação de padrões relevantes entre idade, gênero e risco de doença.

## Conclusão

O pipeline permite analisar grandes volumes de dados de forma eficiente, utilizando processamento incremental e modelos supervisionados, proporcionando insights relevantes para avaliação de idade e risco de doenças.
