# -*- coding: utf-8 -*-
"""Clusterização com K-Means - Titanic"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Carregar os dados
# Na prática, você usaria: dados = pd.read_excel('titanic.csv.xlsx')
dados = pd.read_excel('titanic.csv.xlsx')  # Dados do Titanic

# Selecionar colunas relevantes e tratar valores ausentes
colunas_selecionadas = dados[['Pclass', 'Age', 'Fare']]
imputador = SimpleImputer(strategy='median')
dados_imputados = imputador.fit_transform(colunas_selecionadas)

# Normalizar os dados
escalador = StandardScaler()
dados_normalizados = escalador.fit_transform(dados_imputados)

# Calcular inércia para diferentes valores de k
inercias = []
valores_k = range(1, 11)

for k in valores_k:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(dados_normalizados)
    inercias.append(kmeans.inertia_)

# Plotar o método do cotovelo
plt.figure(figsize=(10, 6))
plt.plot(valores_k, inercias, 'bo-')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inércia')
plt.title('Método do Cotovelo para Determinação do k ideal')
plt.xticks(valores_k)
plt.grid()
plt.show()

# Escolher o k ideal (por exemplo, k = 3 com base no gráfico) e aplicar K-means
k_otimo = 3
kmeans_final = KMeans(n_clusters=k_otimo, random_state=42)
rotulos_clusters = kmeans_final.fit_predict(dados_normalizados)

# Adicionar os clusters ao DataFrame original
dados['Cluster'] = rotulos_clusters

# Analisar os clusters
estatisticas_clusters = dados.groupby('Cluster')[['Pclass', 'Age', 'Fare']].mean()
print(estatisticas_clusters)
