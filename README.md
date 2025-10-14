# Age Assessment & Disease Risk Prediction

Este repositório contém o pipeline completo para avaliação de idade e predição de risco de doenças a partir de dados epigenéticos.

## Estrutura do Projeto

- `preprocessing.py` – scripts para limpeza e transformação dos dados.
- `train_models.py` – treino de modelos de machine learning (SGD, Random Forest).
- `dashboard.py` – visualização interativa dos resultados e clusters.
- `projecto.ipynb` – análise exploratória, PCA e clustering.
- `Relatorio.md` – relatório detalhado do projeto.

## Como Executar

1. Instale as dependências:

-`pandas, numpy, scikit-learn
-seaborn, matplotlib, plotly`
-`pyarrow, joblib
-streamlit (para dashboard interativo)`

2.Pré-processamento:

-`python preprocessing.py`


3.Treinar modelos:

-`python train_models.py`

4. Visualizar resultados:

-`python dashboard.py`



Resultados
Clusters de amostras no espaço PCA.

Predições de doenças com SGDClassifier e RandomForestClassifier.

Matrizes de confusão e métricas de classificação.

Visualizações interativas em Plotly.

Autor
André Jorge




