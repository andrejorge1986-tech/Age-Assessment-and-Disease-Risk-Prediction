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
```bash
pip install -r requirements.txt
Pré-processamento:

bash
Copiar código
python preprocessing.py
Treinar modelos:

bash
Copiar código
python train_models.py
Visualizar resultados:

bash
Copiar código
python dashboard.py
Resultados
Clusters de amostras no espaço PCA.

Predições de doenças com SGDClassifier e RandomForestClassifier.

Matrizes de confusão e métricas de classificação.

Visualizações interativas em Plotly.

Autor
André Jorge

