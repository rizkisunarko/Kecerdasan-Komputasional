# Kecerdasan Komputasional

Repositori ini berisi kumpulan tugas mata kuliah **Kecerdasan Komputasional**. Repositori ini bersifat **berkelanjutan** — folder dan file baru akan terus ditambahkan seiring dengan pengerjaan tugas-tugas berikutnya selama perkuliahan berlangsung.

> 📌 **Catatan:** README ini akan diperbarui setiap kali ada tugas baru yang ditambahkan ke repositori.

---

## 📋 Daftar Tugas

| No | Folder | Topik | Status |
|----|--------|-------|--------|
| 1 | [`Kmeans/`](#-folder-kmeans) | K-Means Clustering | ✅ Selesai |
| 2 | [`TugasAlgoritmaGenetika/`](#-folder-tugasalgoritmagenetika) | Algoritma Genetika — TSP | ✅ Selesai |
| ... | *(akan ditambahkan)* | *(tugas selanjutnya)* | 🔄 Akan Datang |

---

## 📁 Struktur Repositori

> Struktur di bawah ini mencerminkan kondisi repositori saat ini dan akan terus berkembang.

```
Kecerdasan-Komputasional/
├── Kmeans/
│   ├── dataset/
│   │   ├── Mall_Customers.csv
│   │   ├── data_kmeans.csv
│   │   ├── hasil_kmeans_library.csv
│   │   └── hasil_kmeans_scratch.csv
│   ├── image/
│   │   ├── elbow_method_library.png
│   │   ├── hasil_clustering_library.png
│   │   └── hasil_clustering_scratch.png
│   ├── kmeans_library.py
│   ├── kmeans_scratch.py
│   ├── Laporan_Perhitungan_Manual.md
│   └── Panduan_Orange.md
│
├── TugasAlgoritmaGenetika/
│   ├── code/
│   │   ├── tsp_ga.py
│   │   ├── plot_route.py
│   │   └── generate_latex.py
│   ├── media/
│   │   └── best_route.png
│   ├── perhitungan_manual.txt
│   ├── report.tex
│   └── Tugas_KecerdasanKomputasional_Kelompok6_GA_TSP.pdf
│
└── (folder tugas berikutnya akan ditambahkan di sini...)
```

---

## 📂 Folder: `Kmeans`

Berisi implementasi algoritma **K-Means Clustering** untuk mengelompokkan data pelanggan mall berdasarkan *Annual Income* dan *Spending Score*.

### 📁 `dataset/`
| File | Keterangan |
|------|-----------|
| `Mall_Customers.csv` | Dataset asli pelanggan mall yang menjadi sumber data. |
| `data_kmeans.csv` | Dataset yang telah difilter/disiapkan (hanya kolom Annual Income & Spending Score) sebagai input program. |
| `hasil_kmeans_library.csv` | Output hasil clustering menggunakan library Scikit-Learn, berisi label kluster tiap data. |
| `hasil_kmeans_scratch.csv` | Output hasil clustering menggunakan implementasi dari nol (*from scratch*), berisi label kluster tiap data. |

### 📁 `image/`
| File | Keterangan |
|------|-----------|
| `elbow_method_library.png` | Grafik metode Elbow untuk menentukan nilai K optimal (dihasilkan oleh `kmeans_library.py`). |
| `hasil_clustering_library.png` | Visualisasi hasil clustering menggunakan library Scikit-Learn. |
| `hasil_clustering_scratch.png` | Visualisasi hasil clustering menggunakan implementasi dari nol. |

### 🐍 `kmeans_library.py`
Implementasi K-Means Clustering menggunakan library **Scikit-Learn**. Program ini:
- Menerapkan **Metode Elbow** untuk menentukan nilai K optimal.
- Melakukan clustering dengan K=3 menggunakan `sklearn.cluster.KMeans`.
- Menyimpan hasil clustering ke `dataset/hasil_kmeans_library.csv`.
- Menghasilkan grafik Elbow dan visualisasi hasil clustering ke folder `image/`.

### 🐍 `kmeans_scratch.py`
Implementasi K-Means Clustering dari nol (*from scratch*) tanpa menggunakan library machine learning. Program ini:
- Mengimplementasikan perhitungan **Euclidean Distance** secara manual.
- Melakukan iterasi assignment dan update centroid hingga konvergen.
- Menghasilkan laporan **perhitungan manual** langkah demi langkah (Iterasi 1) ke file `Laporan_Perhitungan_Manual.md`.
- Menyimpan hasil clustering ke `dataset/hasil_kmeans_scratch.csv`.

### 📄 `Laporan_Perhitungan_Manual.md`
Laporan perhitungan manual K-Means (K=3) yang dihasilkan otomatis oleh `kmeans_scratch.py`. Berisi:
- Inisialisasi centroid awal.
- Tabel jarak setiap data ke masing-masing centroid pada Iterasi 1.
- Proses pembaruan centroid setelah Iterasi 1.

### 📄 `Panduan_Orange.md`
Panduan langkah-langkah melakukan K-Means Clustering menggunakan aplikasi **Orange Data Mining** (tanpa coding), meliputi import data, visualisasi, penentuan K optimal, dan interpretasi hasil.

---

## 📂 Folder: `TugasAlgoritmaGenetika`

Berisi implementasi **Algoritma Genetika (Genetic Algorithm / GA)** untuk menyelesaikan **Travelling Salesman Problem (TSP)** — mencari rute terpendek yang mengunjungi 15 kota di Amerika Serikat.

### 📁 `code/`
| File | Keterangan |
|------|-----------|
| `tsp_ga.py` | Program utama Algoritma Genetika untuk TSP. |
| `plot_route.py` | Script untuk memvisualisasikan rute terbaik hasil GA ke peta. |
| `generate_latex.py` | Script untuk menghasilkan laporan dalam format LaTeX secara otomatis. |

#### Detail `tsp_ga.py`
Implementasi lengkap Algoritma Genetika dengan:
- **15 kota** di AS (Denver, Las Vegas, Seattle, New York City, dll.).
- **Rank Selection** sebagai metode pemilihan parent.
- **Order Crossover (OX)** sebagai operator crossover.
- **Inversion Mutation** sebagai operator mutasi.
- **Elitism** untuk mempertahankan kromosom terbaik setiap generasi.
- Menghasilkan jejak perhitungan manual ke file `ga_manual_trace.txt`.

Parameter GA:
| Parameter | Nilai |
|-----------|-------|
| Ukuran Populasi | 4 |
| Jumlah Iterasi | 5 |
| Probabilitas Crossover | 0.8 |
| Probabilitas Mutasi | 0.2 |

#### Detail `plot_route.py`
Memvisualisasikan rute TSP terbaik menggunakan `matplotlib`, dengan koordinat kota (latitude/longitude) yang diplot pada bidang 2D. Hasil disimpan ke `media/best_route.png`.

### 📁 `media/`
| File | Keterangan |
|------|-----------|
| `best_route.png` | Visualisasi peta rute terbaik yang ditemukan oleh Algoritma Genetika. |

### 📄 `perhitungan_manual.txt`
File teks berisi jejak perhitungan manual Algoritma Genetika, mencakup evaluasi fitness, proses seleksi, crossover, dan mutasi untuk setiap iterasi/generasi.

### 📄 `report.tex`
Source code laporan dalam format **LaTeX** yang mendeskripsikan metodologi, implementasi, dan hasil eksperimen Algoritma Genetika untuk TSP.

### 📄 `Tugas_KecerdasanKomputasional_Kelompok6_GA_TSP.pdf`
Laporan tugas akhir dalam format PDF (hasil kompilasi dari `report.tex`) milik **Kelompok 6**, menjelaskan secara lengkap implementasi Algoritma Genetika untuk penyelesaian TSP.

---

## 🛠️ Teknologi yang Digunakan

> Teknologi yang digunakan dapat bertambah seiring tugas-tugas baru.

- **Python 3** — bahasa pemrograman utama
- **NumPy** — komputasi numerik
- **Pandas** — manipulasi dan analisis data
- **Matplotlib** — visualisasi grafik
- **Scikit-Learn** — library machine learning (untuk `kmeans_library.py`)
- **Orange Data Mining** — tools visual data mining (panduan penggunaan)
- **LaTeX** — penulisan laporan ilmiah

## ▶️ Cara Menjalankan

### Tugas 1 — K-Means (dari folder `Kmeans/`)
```bash
# Menggunakan library Scikit-Learn
python kmeans_library.py

# Menggunakan implementasi from scratch
python kmeans_scratch.py
```

### Tugas 2 — Algoritma Genetika TSP (dari folder `TugasAlgoritmaGenetika/code/`)
```bash
# Jalankan algoritma genetika
python tsp_ga.py

# Visualisasikan rute terbaik
python plot_route.py
```

> Instruksi untuk tugas-tugas berikutnya akan ditambahkan di sini seiring perkembangan repositori.
