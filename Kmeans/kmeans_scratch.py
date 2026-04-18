import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def euc_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# 1. Load Data
df = pd.read_csv('data_kmeans.csv')
X = df.values

# 2. Inisiasi Parameter K-Means
K = 3
N = X.shape[0]

# Untuk memudahkan ilustrasi perhitungan manual, kita pilih 3 centroid awal dari data
# yaitu baris ke-0, 1, dan 2
centroids = X[:3].copy()
labels = np.zeros(N)

# Persiapkan file laporan perhitungan manual
with open("Laporan_Perhitungan_Manual.md", "w") as f:
    f.write("# Perhitungan Manual K-Means Clustering dengan K=3\n\n")
    f.write(f"Kita menggunakan {N} data yang diambil dari **Mall_Customers** (Fitur: Annual Income & Spending Score).\n")
    f.write("Berdasarkan hasil metode *Elbow*, kita asumsikan **K optimal = 3**.\n")
    f.write("Berikut adalah langkah-langkah perhitungan manual untuk Iterasi 1.\n\n")
    
    f.write("## 1. Inisialisasi Centroid Awal\n")
    f.write("Kita memilih 3 data pertama sebagai centroid awal:\n")
    f.write(f"- Centroid 1 (C1): {centroids[0]}\n")
    f.write(f"- Centroid 2 (C2): {centroids[1]}\n")
    f.write(f"- Centroid 3 (C3): {centroids[2]}\n\n")

    f.write("## 2. Iterasi 1: Menghitung Jarak Data ke Tiap Centroid\n")
    f.write("Kita menggunakan rumus *Euclidean Distance*:\n")
    f.write("d(A, B) = sqrt((x_a - x_b)^2 + (y_a - y_b)^2)\n\n")
    
    # Loop Iterasi (Kita simulasikan lengkap sampai konvergen untuk aplikasi,
    # Namun laporan manual hanya menampilkan Iterasi 1 agar tidak terlalu panjang)
    max_iter = 10
    for iteration in range(max_iter):
        old_centroids = centroids.copy()
        
        if iteration == 0:
            f.write("| Data | Annual Income | Spending Score | Jarak ke C1 | Jarak ke C2 | Jarak ke C3 | Jarak Terdekat | Kluster Baru |\n")
            f.write("| --- | --- | --- | --- | --- | --- | --- | --- |\n")
            
        distances = np.zeros((N, K))
        for i in range(N):
            for j in range(K):
                distances[i, j] = euc_distance(X[i], centroids[j])
            
            # Tentukan kluster terdekat
            labels[i] = np.argmin(distances[i])
            
            if iteration == 0:
                dist_str = [f"{d:.2f}" for d in distances[i]]
                min_dist = np.min(distances[i])
                f.write(f"| Data-{i+1} | {X[i, 0]:.2f} | {X[i, 1]:.2f} | {dist_str[0]} | {dist_str[1]} | {dist_str[2]} | {min_dist:.2f} | C{int(labels[i]+1)} |\n")
        
        # Update Centroid
        if iteration == 0:
            f.write("\n## 3. Iterasi 1: Memperbarui Centroid\n")
            f.write("Centroid baru dihitung dari rata-rata (mean) setiap fitur pada masing-masing kluster:\n\n")
            
        for k in range(K):
            cluster_points = X[labels == k]
            if len(cluster_points) > 0:
                centroids[k] = np.mean(cluster_points, axis=0)
            
            if iteration == 0:
                f.write(f"- **Kluster C{k+1}** memiliki {len(cluster_points)} data.\n")
                if len(cluster_points) > 0:
                    f.write(f"  - C{k+1} Baru = Mean dari {len(cluster_points)} data = [{centroids[k, 0]:.2f}, {centroids[k, 1]:.2f}]\n")
                else:
                    f.write(f"  - Kluster kosong, centroid tidak berubah.\n")
        
        if iteration == 0:
            f.write("\n_Langkah perhitungan jarak dan perbaruan centroid diulang terus hingga centroid tidak berubah (konvergen)._\n\n")

        # Cek konvergensi
        if np.allclose(centroids, old_centroids):
            break

df['Kluster_Scratch'] = labels
df.to_csv('hasil_kmeans_scratch.csv', index=False)
print("Klastering Scratch Berhasil. Konvergen pada iterasi ke-", iteration + 1)
print("Manual Trace untuk Iterasi 1 telah ditulis ke 'Laporan_Perhitungan_Manual.md'.")

# Visualisasi
plt.figure(figsize=(8, 5))
warna = ['r', 'g', 'b']
for i in range(3):
    plt.scatter(X[labels == i, 0], X[labels == i, 1], s=50, c=warna[i], label=f'Kluster {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='yellow', marker='*', edgecolor='black', label='Centroid Akhir')
plt.title('Hasil K-Means Clustering (K=3) dari Program Scratch (Perhitungan Manual)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True)
plt.savefig('hasil_clustering_scratch.png')
print("Grafik klastering scratch disimpan sebagai 'hasil_clustering_scratch.png'.")
