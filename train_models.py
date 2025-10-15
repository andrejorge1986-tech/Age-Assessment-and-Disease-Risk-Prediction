
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# ===== CONFIGURAÇÃO =====
SRC_DIR = r"C:\Users\andr3\Documents\DATA SCIENCE\10794 - Programação avançada com Python\Age Assessment & Disease Risk Prediction\src"
CLEAN_FOLDER = os.path.join(SRC_DIR, "clean")
PARQUET_FILE = os.path.join(CLEAN_FOLDER, "train_processed.parquet")
MODEL_PATH = os.path.join(CLEAN_FOLDER, "model_sgd.pkl")

# ===== CARREGAR DADOS =====
df = pd.read_parquet(PARQUET_FILE)

# ===== PREPARAR FEATURES E TARGET =====
X = df[["PC1", "PC2"]].astype("float32")

# Codificar target (doença)
le = LabelEncoder()
df["target"] = le.fit_transform(df["disease"].astype(str))
y = df["target"].astype("int32")

# ===== INICIALIZAR MODELO =====
model = SGDClassifier(loss="log_loss", random_state=42)

# ===== TREINAR EM MINI-BATCHES =====
BATCH_SIZE = 1000
for i in range(0, len(X), BATCH_SIZE):
    X_batch = X.iloc[i:i+BATCH_SIZE]
    y_batch = y.iloc[i:i+BATCH_SIZE]
    model.partial_fit(X_batch, y_batch, classes=np.unique(y))

# ===== SALVAR MODELO =====
joblib.dump(model, MODEL_PATH)
print(f"✅ Modelo supervisionado salvo em: {MODEL_PATH}")
