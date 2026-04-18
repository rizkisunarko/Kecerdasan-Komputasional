# Panduan Penggunaan Orange Data Mining untuk K-Means

Berikut adalah langkah-langkah untuk melakukan _clustering_ K-Means dan menemukan metode Elbow pada Orange Data Mining menggunakan dataset `data_kmeans.csv` yang telah disediakan.

## Langkah-langkah:

1. **Mempersiapkan Data (File)**
   - Buka aplikasi **Orange Data Mining**.
   - Dari menu widget sebelah kiri (kategori **Data**), tarik widget **CSV File Import** atau **File** ke dalam kanvas.
   - Klik ganda (double-click) pada widget tersebut.
   - Pilih file `dataset/data_kmeans.csv` (pastikan tipe data untuk `Annual_Income` dan `Spending_Score` terdeteksi sebagai _Numeric_).

2. **Memvisualisasikan Data Awal**
   - Tarik widget **Scatter Plot** dari kategori **Visualize**.
   - Hubungkan garis dari widget **File** ke **Scatter Plot**.
   - Buka **Scatter Plot** untuk melihat bagaimana titik-titik data tersebar sebelum diklasterkan. Anda akan melihat indikasi adanya 3 kelompok yang terpisah.

3. **Menemukan K Optimal (Metode Silhouette / Elbow)**
   *Catatan: Orange secara default lebih menekankan analisis Silhouette untuk penentuan K, namun ini serupa dengan prinsip Elbow.*
   - Tarik widget **K-Means** dari kategori **Unsupervised**.
   - Hubungkan widget **File** ke widget **K-Means**.
   - Klik ganda pada widget **K-Means**.
   - Pada bagian **Number of clusters**, jangan pilih angka tetap secara manual terlebih dahulu, centang opsi **Optimize from _2_ to _8_** (atau angka lainnya) dan perhatikan nilai skor Silhouette yang muncul di bawahnya. 
   - Skor tertinggi akan menunjukkan jumlah kluster paling optimal. Sebagaimana yang diminta pada tugas, _K optimal yang paling dominan kemungkinan adalah 3_.
   - Setelah selesai mengobservasi, set secara manual **Fixed: 3** kluster.

4. **Melihat Hasil Clustering K-Means**
   - Tarik kembali widget **Scatter Plot** (atau gunakan yang sudah ada).
   - Hubungkan output dari widget **K-Means** ke **Scatter Plot** tersebut.
   - Buka widget **Scatter Plot**.
   - Pada panel sebelah kiri di dalam Scatter Plot, atur **Color** berdasarkan `Cluster` (variabel target yang dibuat otomatis oleh widget K-Means).
   - Atur **Shape** berdasarkan `Cluster` jika diperlukan.
   - Pada tampilan ini, Anda bisa melihat dengan jelas bagaimana data telah dipisah menjadi 3 warna (3 kluster).

5. **Menyimpan Format Data yang Telah Diklasterisasi (Opsional)**
   - Jika membutuhkan output berformat tabel yang dilengkapi hasil klasternya, tarik widget **Data Table**.
   - Hubungkan dari widget **K-Means** ke **Data Table**.
   - Klik ganda **Data Table** untuk melihat baris-baris data yang kini memiliki kolom tambahan `Cluster`.
   - Tarik widget **Save Data** untuk mengekspor tabel tersebut ke bentuk CSV berisikan label kluster jika diperlukan.
