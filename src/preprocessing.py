import os
import pandas as pd
import numpy as np
from sklearn.decomposition import IncrementalPCA
from sklearn.cluster import MiniBatchKMeans

# ===== CONFIGURAÇÃO =====
SRC_DIR = r"C:\Users\andr3\Documents\DATA SCIENCE\10794 - Programação avançada com Python\Age Assessment & Disease Risk Prediction\src"
CLEAN_FOLDER = os.path.join(SRC_DIR, "clean")
os.makedirs(CLEAN_FOLDER, exist_ok=True)

TRAIN_FILE = os.path.join(SRC_DIR, "traindata.csv")
TRAINMAP_FILE = os.path.join(SRC_DIR, "trainmap.csv")
OUTPUT_FILE = os.path.join(CLEAN_FOLDER, "train_processed.parquet")

# ===== PARÂMETROS =====
CHUNK_SIZE = 10000
N_COMPONENTS = 2
N_CLUSTERS = 4

# ===== CARREGAR METADADOS =====
trainmap_df = pd.read_csv(TRAINMAP_FILE, usecols=["age", "gender", "sample_type", "disease"])
trainmap_df["sample_id"] = trainmap_df.index.astype(str)

# ===== INICIALIZAR PCA E KMEANS =====
pca = IncrementalPCA(n_components=N_COMPONENTS)
kmeans = MiniBatchKMeans(n_clusters=N_CLUSTERS, random_state=42, batch_size=500)

# ===== TREINAR PCA =====
print("🔄 Treinando PCA...")
for chunk in pd.read_csv(TRAIN_FILE, chunksize=CHUNK_SIZE, usecols=lambda c: c.startswith("train")):
    chunk = chunk.fillna(0).astype("float32")
    pca.partial_fit(chunk)
print("✅ PCA treinado.")

# ===== TRANSFORMAR E CLUSTERIZAR =====
print("🔄 Aplicando PCA e KMeans...")
results = []
sample_counter = 0

for chunk in pd.read_csv(TRAIN_FILE, chunksize=CHUNK_SIZE):
    feature_cols = [c for c in chunk.columns if c.startswith("train")]
    chunk_features = chunk[feature_cols].fillna(0).astype("float32")

    chunk["sample_id"] = np.arange(sample_counter, sample_counter + len(chunk)).astype(str)
    sample_counter += len(chunk)

    chunk["PC1"], chunk["PC2"] = pca.transform(chunk_features).T
    chunk["cluster"] = kmeans.partial_fit(chunk_features).predict(chunk_features)

    results.append(chunk[["sample_id", "PC1", "PC2", "cluster"]])
    del chunk, chunk_features

# ===== MERGE COM METADADOS =====
final_df = pd.concat(results, ignore_index=True)
final_df = final_df.merge(trainmap_df, on="sample_id", how="left")

# ===== SALVAR =====
final_df.to_parquet(OUTPUT_FILE, index=False)
print("✅ Arquivo salvo em:", OUTPUT_FILE)