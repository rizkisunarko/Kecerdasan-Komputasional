import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load Data
df = pd.read_csv('dataset/data_kmeans.csv')
X = df.values

# Elbow Method untuk menentukan K optimal
wcss = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, init='random', random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, wcss, marker='o', linestyle='--')
plt.title('Metode Elbow untuk Menentukan K Optimal')
plt.xlabel('Jumlah Kluster (K)')
plt.ylabel('WCSS (Penjumlahan Kuadrat Jarak)')
plt.xticks(K_range)
plt.grid(True)
plt.savefig('image/elbow_method_library.png')
print("Grafik metode Elbow telah disimpan sebagai 'image/elbow_method_library.png'.")

# Dari grafik Elbow, didapatkan bahwa patahan (elbow) signifikan ada di K=3.
print("\nBerdasarkan Metode Elbow, kita pilih K = 3.")

# K-Means dengan K=3
kmeans_optimal = KMeans(n_clusters=3, init='random', random_state=42, n_init=10)
kmeans_optimal.fit(X)
labels = kmeans_optimal.labels_
centroids = kmeans_optimal.cluster_centers_

# Menyimpan hasil
df['Kluster'] = labels
print("\nHasil Klastering Pustaka/Library (5 data pertama):")
print(df.head())
df.to_csv('dataset/hasil_kmeans_library.csv', index=False)

# Visualisasi Hasil
plt.figure(figsize=(8, 5))
warna = ['r', 'g', 'b']
for i in range(3):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], s=50, c=warna[i], label=f'Kluster {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='yellow', marker='*', edgecolor='black', label='Centroid')
plt.title('Hasil K-Means Clustering (K=3) menggunakan Library Scikit-Learn')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)
plt.savefig('image/hasil_clustering_library.png')
print("\nVisualisasi klastering telah disimpan sebagai 'image/hasil_clustering_library.png'.")
