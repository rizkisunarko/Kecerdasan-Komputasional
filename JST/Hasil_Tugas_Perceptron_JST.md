# Tugas Jaringan Saraf Tiruan - Logika AND & OR dengan Perceptron

Berikut adalah hasil penyelesaian tugas logika AND dan OR menggunakan algoritma Perceptron dengan fungsi aktivasi Step Function.

## 1. Aturan dan Parameter
1. **Fungsi Aktivasi (Step Function)**:
   * $f(net) = 0$ jika $net < 0$
   * $f(net) = 1$ jika $net \ge 0$
2. **Kondisi Berhenti**: Dilatih hingga error pada suatu epoch bernilai $0$ untuk semua data (seluruh data berhasil diklasifikasikan dengan benar).
3. **Variasi Learning Rate ($\alpha$)**:
   * Pembelajaran 1: $\alpha = 0.1$
   * Pembelajaran 2: $\alpha = 0.01$
   * Pembelajaran 3: $\alpha = 0.001$

Bobot ($w_1$, $w_2$) dan bias ($b$) awal diinisialisasi dengan $0$.
Rumus pembaruan bobot (jika error $\neq 0$):
* $\Delta w = \alpha \times error \times x$
* $\Delta b = \alpha \times error$
dimana $error = target - output$.

---

## 2. Tabel Kebenaran (Data Latih)

### Logika AND
| $x_1$ | $x_2$ | Target |
|-------|-------|--------|
|   0   |   0   |   0    |
|   0   |   1   |   0    |
|   1   |   0   |   0    |
|   1   |   1   |   1    |

### Logika OR
| $x_1$ | $x_2$ | Target |
|-------|-------|--------|
|   0   |   0   |   0    |
|   0   |   1   |   1    |
|   1   |   0   |   1    |
|   1   |   1   |   1    |

---

## 3. Analisa Hasil Pembelajaran

Setelah dilatih dengan Python Script (`perceptron.py`), berikut adalah rekapitulasi konvergensinya:

### Ringkasan Konvergensi
| Logika | $\alpha$ | Epoch Berhenti | Bobot Akhir ($w_1, w_2$) | Bias Akhir ($b$) |
|--------|----------|----------------|--------------------------|------------------|
| **AND**| $0.1$    | **6**          | $[0.2,\; 0.1]$           | $-0.3$           |
| **AND**| $0.01$   | **6**          | $[0.02,\; 0.01]$         | $-0.03$          |
| **AND**| $0.001$  | **6**          | $[0.002,\; 0.001]$       | $-0.003$         |
| **OR** | $0.1$    | **4**          | $[0.1,\; 0.1]$           | $-0.1$           |
| **OR** | $0.01$   | **4**          | $[0.01,\; 0.01]$         | $-0.01$          |
| **OR** | $0.001$  | **4**          | $[0.001,\; 0.001]$       | $-0.001$         |

### Analisa Penting:
1. **Jumlah Epoch Sama**: Terlihat bahwa variasi learning rate ($0.1$, $0.01$, dan $0.001$) **tidak mengubah kecepatan konvergensi** (AND tetap butuh 6 epoch, OR tetap butuh 4 epoch). 
2. **Skalabilitas Bobot**: Hal ini terjadi karena inisialisasi awal bobot dan bias adalah $0$, sehingga seluruh pembaruan bobot hanya dikalikan secara proporsional dengan $\alpha$. Karena kondisi pada fungsi aktivasi adalah $net \ge 0$, maka hasil $w \times \alpha$ tidak mengubah tanda / polaritas dari nilai $net$. (Misal: $net$ bernilai $0.2 \ge 0$ pada $\alpha=0.1$ memiliki arti logika yang sama persis dengan $net$ bernilai $0.002 \ge 0$ pada $\alpha=0.001$).
3. **Tingkat Kesulitan**: Logika AND membutuhkan jumlah epoch (6 epoch) yang lebih banyak dari OR (4 epoch). Hal ini menandakan bahwa batas keputusan (decision boundary) untuk memisahkan data pada logika AND memakan proses iterasi penyesuaian yang sedikit lebih banyak dibanding logika OR.

---

## 4. Perhitungan Manual (Contoh dengan $\alpha = 0.1$)

Untuk menghindari tulisan yang terlalu panjang, berikut adalah simulasi langkah demi langkah untuk epoch awal.

### A. Perhitungan Manual Logika OR ($\alpha = 0.1$)
**Inisialisasi**: $w_1 = 0, w_2 = 0, b = 0$

**Epoch 1:**
1. Data 1: $x_1=0, x_2=0$, Target$=0$
   * $net = (0 \times 0) + (0 \times 0) + 0 = 0$
   * Output = $f(0) = 1$
   * Error = $0 - 1 = -1$ (Update!)
   * $w_1 = 0 + 0.1(-1)(0) = 0$
   * $w_2 = 0 + 0.1(-1)(0) = 0$
   * $b = 0 + 0.1(-1) = -0.1$
2. Data 2: $x_1=0, x_2=1$, Target$=1$
   * $net = (0 \times 0) + (0 \times 1) + (-0.1) = -0.1$
   * Output = $f(-0.1) = 0$
   * Error = $1 - 0 = 1$ (Update!)
   * $w_1 = 0 + 0.1(1)(0) = 0$
   * $w_2 = 0 + 0.1(1)(1) = 0.1$
   * $b = -0.1 + 0.1(1) = 0$
3. Data 3: $x_1=1, x_2=0$, Target$=1$
   * $net = (0 \times 1) + (0.1 \times 0) + 0 = 0$
   * Output = $f(0) = 1$
   * Error = $1 - 1 = 0$ (Tidak ada update)
4. Data 4: $x_1=1, x_2=1$, Target$=1$
   * $net = (0 \times 1) + (0.1 \times 1) + 0 = 0.1$
   * Output = $f(0.1) = 1$
   * Error = $1 - 1 = 0$ (Tidak ada update)

*(Proses ini berlanjut hingga seluruh data pada **Epoch 4** menghasilkan Error = 0. Pada Epoch 4 tersebut, bobot akhir yang didapat stabil di $w_1=0.1, w_2=0.1, b=-0.1$)*.

### B. Perhitungan Manual Logika AND ($\alpha = 0.1$)
**Inisialisasi**: $w_1 = 0, w_2 = 0, b = 0$

**Epoch 1:**
1. Data 1: $x_1=0, x_2=0$, Target$=0$
   * $net = (0 \times 0) + (0 \times 0) + 0 = 0$
   * Output = $f(0) = 1$
   * Error = $0 - 1 = -1$ (Update!)
   * $w_1 = 0, w_2 = 0, b = -0.1$
2. Data 2: $x_1=0, x_2=1$, Target$=0$
   * $net = (0 \times 0) + (0 \times 1) - 0.1 = -0.1$
   * Output = $f(-0.1) = 0$
   * Error = $0 - 0 = 0$ (Tidak update)
3. Data 3: $x_1=1, x_2=0$, Target$=0$
   * $net = (0 \times 1) + (0 \times 0) - 0.1 = -0.1$
   * Output = $f(-0.1) = 0$
   * Error = $0 - 0 = 0$ (Tidak update)
4. Data 4: $x_1=1, x_2=1$, Target$=1$
   * $net = (0 \times 1) + (0 \times 1) - 0.1 = -0.1$
   * Output = $f(-0.1) = 0$
   * Error = $1 - 0 = 1$ (Update!)
   * $w_1 = 0 + 0.1(1)(1) = 0.1$
   * $w_2 = 0 + 0.1(1)(1) = 0.1$
   * $b = -0.1 + 0.1(1) = 0$

**Epoch 2:**
1. Data 1: $x_1=0, x_2=0$, Target$=0$
   * $net = (0.1 \times 0) + (0.1 \times 0) + 0 = 0$
   * Output = $f(0) = 1$
   * Error = $0 - 1 = -1$ (Update!)
   * $w_1 = 0.1, w_2 = 0.1, b = -0.1$
2. Data 2: $x_1=0, x_2=1$, Target$=0$
   * $net = (0.1 \times 0) + (0.1 \times 1) - 0.1 = 0$
   * Output = $f(0) = 1$
   * Error = $0 - 1 = -1$ (Update!)
   * $w_1 = 0.1, w_2 = 0, b = -0.2$
3. Data 3: $x_1=1, x_2=0$, Target$=0$
   * $net = (0.1 \times 1) + (0 \times 0) - 0.2 = -0.1$
   * Output = $f(-0.1) = 0$
   * Error = $0 - 0 = 0$ (Tidak update)
4. Data 4: $x_1=1, x_2=1$, Target$=1$
   * $net = (0.1 \times 1) + (0 \times 1) - 0.2 = -0.1$
   * Output = $f(-0.1) = 0$
   * Error = $1 - 0 = 1$ (Update!)
   * $w_1 = 0.2, w_2 = 0.1, b = -0.1$

*(Proses ini berlanjut hingga **Epoch 6** di mana tidak ada lagi error (Error = 0 pada semua iterasi data).*
