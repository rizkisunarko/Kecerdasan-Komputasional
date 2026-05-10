# Hasil Tugas Kelompok: Multi-Layer Perceptron (MLP)

## 1. Deskripsi Dataset dan Arsitektur Jaringan

*   **Dataset:** Dataset `Iris.csv` yang diambil dari Kaggle. Karena diminta 2 kelas dan 50 baris, kami mengambil 25 baris dari kelas `Iris-versicolor` (Kelas 2) dan 25 baris dari `Iris-virginica` (Kelas 3), total 50 baris. Berikut adalah cuplikan 10 baris datanya:

| SepalLength ($X_1$) | SepalWidth ($X_2$) | PetalLength ($X_3$) | PetalWidth ($X_4$) | Species / Kelas |
| :---: | :---: | :---: | :---: | :--- |
| 7.0 | 3.2 | 4.7 | 1.4 | Iris-versicolor |
| 6.4 | 3.2 | 4.5 | 1.5 | Iris-versicolor |
| 6.9 | 3.1 | 4.9 | 1.5 | Iris-versicolor |
| 5.5 | 2.3 | 4.0 | 1.3 | Iris-versicolor |
| 6.5 | 2.8 | 4.6 | 1.5 | Iris-versicolor |
| 6.3 | 3.3 | 6.0 | 2.5 | Iris-virginica |
| 5.8 | 2.7 | 5.1 | 1.9 | Iris-virginica |
| 7.1 | 3.0 | 5.9 | 2.1 | Iris-virginica |
| 6.3 | 2.9 | 5.6 | 1.8 | Iris-virginica |
| 6.5 | 3.0 | 5.8 | 2.2 | Iris-virginica |

*   **Fitur (X):** Terdapat 4 fitur yaitu `SepalLengthCm`, `SepalWidthCm`, `PetalLengthCm`, dan `PetalWidthCm`.
*   **Target (Y):** 2 kelas yang di-encode menggunakan *one-hot encoding*. Kelas 2 merepresentasikan output Neuron 1 aktif `[1, 0]`, sedangkan Kelas 3 merepresentasikan output Neuron 2 aktif `[0, 1]`.
*   **Arsitektur JST:**
    *   **Layer Input:** 4 neuron input + 1 bias
    *   **Hidden Layer:** 1 layer dengan 2 neuron + 1 bias
    *   **Layer Output:** 1 layer dengan 2 neuron (untuk kelas 2 dan kelas 3)
    *   **Fungsi Aktivasi:** Sigmoid (baik di hidden layer maupun output layer)

## 2. Hasil Greedy Search (Grid Search) Parameter

Telah dilakukan pengujian terhadap seluruh kombinasi parameter *Epoch* (10, 100, 500) dan *Learning Rate* (0.1, 0.01, 0.001). Berikut adalah hasil akurasinya pada 50 data tersebut (1 kali percobaan per kombinasi):

| Epochs | Learning Rate | Akurasi (%) |
| :--- | :--- | :--- |
| 10 | 0.1 | 84.00% |
| 10 | 0.01 | 50.00% |
| 10 | 0.001 | 50.00% |
| 100 | 0.1 | 50.00% |
| 100 | 0.01 | 80.00% |
| 100 | 0.001 | 50.00% |
| 500 | 0.1 | 52.00% |
| 500 | 0.01 | 100.00% |
| 500 | 0.001 | 78.00% |

Berdasarkan hasil di atas, model mencapai akurasi tertinggi sebesar **100%** pada konfigurasi *Epoch* 500 dan *Learning Rate* 0.01.

---

## 3. Perhitungan Manual Feedforward dan Backpropagation (1 Epoch, 1 Baris Pertama)

Perhitungan manual dilakukan pada 1 baris pertama (*Iris-versicolor*) dengan `Learning Rate = 0.1`.

### A. Inisialisasi
*   **Input (X):** `[7.0, 3.2, 4.7, 1.4]`
*   **Target (Y):** `[1, 0]` (karena ini adalah Iris-versicolor / kelas 2)
*   **Bobot Input ke Hidden (W1) & Bias (b1):**
    ```text
    W1 = [[-0.125,  0.450]
          [ 0.231,  0.098]
          [-0.343, -0.344]
          [-0.441,  0.366]]
    b1 = [[ 0.101,  0.208]]
    ```
*   **Bobot Hidden ke Output (W2) & Bias (b2):**
    ```text
    W2 = [[-0.479,  0.469]
          [ 0.332, -0.287]]
    b2 = [[-0.318, -0.316]]
    ```

### B. Proses Feedforward

**1. Menghitung Input pada Hidden Layer (z1)**
$$z1 = (X \cdot W1) + b1$$
$z1_{1} = (7.0 \times -0.125) + (3.2 \times 0.231) + (4.7 \times -0.343) + (1.4 \times -0.441) + 0.101 = -2.270$
$z1_{2} = (7.0 \times 0.450) + (3.2 \times 0.098) + (4.7 \times -0.344) + (1.4 \times 0.366) + 0.208 = 2.574$

**2. Menghitung Output pada Hidden Layer (a1) dengan fungsi Sigmoid**
$$a1 = \frac{1}{1 + e^{-z1}}$$
$a1_{1} = \frac{1}{1 + e^{2.270}} = 0.0936$
$a1_{2} = \frac{1}{1 + e^{-2.574}} = 0.9292$

**3. Menghitung Input pada Output Layer (z2)**
$$z2 = (a1 \cdot W2) + b2$$
$z2_{1} = (0.0936 \times -0.479) + (0.9292 \times 0.332) + (-0.318) = -0.0541$
$z2_{2} = (0.0936 \times 0.469) + (0.9292 \times -0.287) + (-0.316) = -0.5398$

**4. Menghitung Final Output (a2) dengan fungsi Sigmoid**
$$a2 = \frac{1}{1 + e^{-z2}}$$
$a2_{1} = \frac{1}{1 + e^{0.0541}} = 0.4864$
$a2_{2} = \frac{1}{1 + e^{0.5398}} = 0.3682$
*Output dari model saat ini adalah [0.4864, 0.3682], belum mencapai target [1, 0].*

### C. Proses Backpropagation

**1. Menghitung Error dan Delta pada Output Layer ($\delta_2$)**
$\text{Error} = Target - a2$
$\text{Error}_1 = 1 - 0.4864 = 0.5135$
$\text{Error}_2 = 0 - 0.3682 = -0.3682$

Turunan sigmoid: $a2 \times (1 - a2)$
$\delta_{2,1} = \text{Error}_1 \times a2_{1} \times (1 - a2_{1}) = 0.5135 \times 0.4864 \times 0.5136 = 0.1282$
$\delta_{2,2} = \text{Error}_2 \times a2_{2} \times (1 - a2_{2}) = -0.3682 \times 0.3682 \times 0.6318 = -0.0856$

**2. Menghitung Error dan Delta pada Hidden Layer ($\delta_1$)**
$\text{Error}_{\text{hidden}} = \delta_2 \cdot W2^T$
$\text{Error}_{\text{hidden},1} = (0.1282 \times -0.479) + (-0.0856 \times 0.469) = -0.1017$
$\text{Error}_{\text{hidden},2} = (0.1282 \times 0.332) + (-0.0856 \times -0.287) = 0.0672$

$\delta_1 = \text{Error}_{\text{hidden}} \times a1 \times (1 - a1)$
$\delta_{1,1} = -0.1017 \times 0.0936 \times (1 - 0.0936) = -0.0086$
$\delta_{1,2} = 0.0672 \times 0.9292 \times (1 - 0.9292) = 0.0044$

### D. Pembaruan Bobot dan Bias (Update Weights)
*Rumus:* $W_{\text{new}} = W_{\text{old}} + (Input^T \cdot \delta \times lr)$

**1. Update Bobot Hidden ke Output (W2) & Bias (b2)**
$W2_{\text{new}} = W2 + (a1^T \cdot \delta_2 \times 0.1)$
```text
W2_new = [[-0.478,  0.469]
          [ 0.344, -0.295]]
b2_new = [[-0.305, -0.325]]
```

**2. Update Bobot Input ke Hidden (W1) & Bias (b1)**
$W1_{\text{new}} = W1 + (X^T \cdot \delta_1 \times 0.1)$
```text
W1_new = [[-0.131,  0.453]
          [ 0.229,  0.100]
          [-0.348, -0.341]
          [-0.443,  0.366]]
b1_new = [[ 0.100,  0.208]]
```
*Bobot inilah yang akan digunakan untuk proses iterasi (baris/epoch) selanjutnya.*
