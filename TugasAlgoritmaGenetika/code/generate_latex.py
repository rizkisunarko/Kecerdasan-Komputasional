import csv
import math
import random
import sys

POP_SIZE = 4
ITERATIONS = 5
PC = 0.8
PM = 0.2
SEED = 42
random.seed(SEED)

def euclidean_distance(city1, city2):
    return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

def calculate_route_distance(route, dist_matrix):
    total = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    total += dist_matrix[route[-1]][route[0]]
    return total

def rank_selection(population, fitness):
    sorted_pop = [x for _, x in sorted(zip(fitness, population), reverse=True)]
    n = len(sorted_pop)
    ranks = list(range(1, n + 1))
    rank_probs = [rank / sum(ranks) for rank in reversed(ranks)]
    cum_probs = []
    tot = 0
    for p in rank_probs:
        tot += p
        cum_probs.append(tot)
    parents = []
    for _ in range(2):
        r = random.random()
        for i, cp in enumerate(cum_probs):
            if r <= cp:
                parents.append(sorted_pop[i])
                break
    return parents, sorted_pop, rank_probs, cum_probs

def order_crossover(p1, p2):
    n = len(p1)
    c1, c2 = random.sample(range(n), 2)
    s, e = min(c1, c2), max(c1, c2)
    child = [-1] * n
    child[s:e+1] = p1[s:e+1]
    p2_idx = (e + 1) % n
    child_idx = (e + 1) % n
    while -1 in child:
        if p2[p2_idx] not in child:
            child[child_idx] = p2[p2_idx]
            child_idx = (child_idx + 1) % n
        p2_idx = (p2_idx + 1) % n
    return child, s, e

def inversion_mutation(ind):
    n = len(ind)
    c1, c2 = random.sample(range(n), 2)
    s, e = min(c1, c2), max(c1, c2)
    mutated = ind[:]
    mutated[s:e+1] = reversed(mutated[s:e+1])
    return mutated, s, e

def create_latex():
    cities = [
        ("Denver",39.7420,-104.9915), ("Colorado Springs",38.8461,-104.8006),
        ("Telluride",37.9375,-107.8123), ("Las Vegas",36.1146,-115.1728),
        ("Grand Canyon",36.0565,-112.1251), ("Yellowstone NP",44.4237,-110.5885),
        ("Mount Rushmore",43.9686,-103.3818), ("Seattle",47.6080,-122.3352),
        ("Redwood NP",41.2131,-124.0046), ("San Diego",32.7157,-117.1610),
        ("Los Angeles",34.05223,-118.24368), ("Mount Hood NF",45.454350,-121.933136),
        ("Santa Fe",35.691544,-105.944183), ("Chicago",41.881832,-87.623177),
        ("New York City",40.730610,-73.935242)
    ]
    n_cities = len(cities)
    dist_matrix = [[0]*n_cities for _ in range(n_cities)]
    for i in range(n_cities):
        for j in range(n_cities):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            
    population = [list(range(n_cities)) for _ in range(POP_SIZE)]
    for p in population:
        random.shuffle(p)
        
    best_overall_dist = float('inf')
    best_overall_route = []

    tex = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{hyperref}

\title{\textbf{Tugas Algoritma Genetika --- Studi Kasus TSP}}
\author{
  \textbf{Kelompok 6} \\
  1. Rizki Pratama Sunarko(240411100181) \\
  2. Ainur Suharyanto (240411100154)\\
  3. Wahyu Ari Ananda Fitrotul Huda (240411100148)\\
}
\date{}

\begin{document}
\maketitle

\section{Pendahuluan}
Studi kasus ini menyelesaikan \textit{Traveling Salesperson Problem} (TSP) menggunakan Algoritma Genetika, bukan optimasi fungsi $x^2$. Data yang diproses berupa koordinat dari 15 kota di Amerika Serikat. Algoritma genetika diimplementasikan dengan spesifikasi:
\begin{itemize}
    \item \textbf{Seleksi}: Rank Selection
    \item \textbf{Crossover}: Order Crossover (OX)
    \item \textbf{Mutasi}: Inversion Mutation
    \item \textbf{Elitism}: Mempertahankan individu terbaik di setiap generasi
    \item \textbf{Jumlah Iterasi}: 5
    \item \textbf{Ukuran Populasi}: 4 Kromosom (untuk mempermudah perhitungan manual)
    \item \textbf{Peluang Crossover ($P_c$)}: 0.8
    \item \textbf{Peluang Mutasi ($P_m$)}: 0.2
\end{itemize}

\section{Data Kota}
Berikut adalah daftar 15 kota beserta indeksnya yang digunakan sebagai representasi gen pada kromosom.
\begin{table}[h!]\centering
\begin{tabular}{clcc}
\toprule
\textbf{Indeks} & \textbf{Kota} & \textbf{Latitude} & \textbf{Longitude} \\
\midrule
"""
    for i, c in enumerate(cities):
        tex += f"{i} & {c[0]} & {c[1]:.4f} & {c[2]:.4f} \\\\\n"
    tex += r"""\bottomrule
\end{tabular}
\end{table}

\section{Metodologi dan Deskripsi Parameter}
\textbf{1. Representasi Kromosom}\\ Pendekatan urutan jarak lokasi antar titik (TSP) lebih natural dan intuitif untuk dikerjakan dalam bentuk permutasi. Sebuah gen merupakan salah satu dari nilai \textit{integer} $0$ hingga $14$ (panjang kromosom = 15 gen tak berulang).
\vspace{0.2cm}

\textbf{2. Fitness Function}\\ Karena pencarian TSP terfokus pada mencari lintasan sirkuit terpendek dalam suatu graph berarah (minimasi jarak), evaluasi fitness dihitung berdasarkan kebalikan (\textit{inverse}) dari total \textit{Euclidean distance}.
\[ \text{Fitness} = \frac{1}{\sum_{i=1}^{n} d(city_i, city_{i+1})} \]
\vspace{0.2cm}

\textbf{3. Rank Selection}\\ Mekanisme probabilitas peluang disesuaikan pada porsi rank sebuah populasi sehingga jika terdapat suatu individu yang fitness-nya dominan (\textit{super individual}), ia tidak akan merusak keragaman gen kromosom lainnya secara radikal (\textit{premature convergence}).
\vspace{0.2cm}

\textbf{4. Order Crossover (OX)}\\ Operator ini dirancang khusus urutan bilangan. Memilih batas substring dari salah satu induk dan mewarisinya pada posisi awal (sebagai segmen utama). Adapun elemen kota sisanya akan diambil secara bertahap dalam susunan order gen induk kedua tanpa adanya kondisi elemen kembar (\textit{duplicated genes}).
\vspace{0.2cm}

\textbf{5. Inversion Mutation}\\ Menentukan batasan acak titik awal dan akhir, lantas membalik (inverse/reverse) blok rute pada posisi tersebut guna menambah keunikan genotip keturunan dan melarikan dinamis dari ruang optimasi lokal.
\vspace{0.2cm}

\section{Matriks Jarak Antarkota (Euclidean Distance Matrix)}
Tabel di bawah memperlihatkan jarak Euclid yang dihitung dengan rumus persamaan $d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$. Tabel ini merepresentasikan bentukan graph terhubung sempurna berbobot (\textit{Fully-connected Weighted Graph}) antar ke-15 titik kota.

\begin{table}[h!]\centering
\resizebox{\linewidth}{!}{
\begin{tabular}{c|*{15}{c}}
\toprule
\textbf{Kota} & \textbf{0} & \textbf{1} & \textbf{2} & \textbf{3} & \textbf{4} & \textbf{5} & \textbf{6} & \textbf{7} & \textbf{8} & \textbf{9} & \textbf{10} & \textbf{11} & \textbf{12} & \textbf{13} & \textbf{14} \\
\midrule
"""
    for i in range(n_cities):
        tex += f"\\textbf{{{i}}}"
        for j in range(n_cities):
            tex += f" & {dist_matrix[i][j]:.2f}"
        tex += " \\\\\n"
    
    tex += r"""\bottomrule
\end{tabular}
}
\end{table}

\section{Perhitungan Manual (5 Iterasi)}
"""
    for it in range(ITERATIONS):
        tex += f"\\subsection*{{Iterasi {it+1}}}\n"
        tex += "\\textbf{1. Evaluasi Fitness}\\\\$Fitness = 1 / Total Jarak$\n"
        tex += "\\begin{itemize}\n"
        
        distances = [calculate_route_distance(p, dist_matrix) for p in population]
        fitness = [1/d for d in distances]
        for i, (p, d, fit) in enumerate(zip(population, distances, fitness)):
            tex += f"\\item K{i+1}: {p} $\\rightarrow$ Jarak: {d:.2f}, Fitness: {fit:.6f}\n"
        tex += "\\end{itemize}\n"
        
        best_idx = distances.index(min(distances))
        if distances[best_idx] < best_overall_dist:
            best_overall_dist = distances[best_idx]
            best_overall_route = population[best_idx][:]
            
        tex += "\\vspace{0.5cm}\\textbf{2. Rank Selection}\\\\"
        parents, sorted_pop, rank_probs, cum_probs = rank_selection(population, fitness)
        tex += "Kromosom diurutkan berdasarkan fitness (tertinggi ke terendah) dan diberi rank:\n"
        tex += "\\begin{table}[h!]\\centering\\begin{tabular}{ccccc}\\toprule Rank & Kromosom & Probabilitas & Kumulatif Probabilitas \\\\ \\midrule\n"
        for i, sp in enumerate(sorted_pop):
            tex += f"{len(sorted_pop)-i} & {sp} & {rank_probs[i]:.2f} & {cum_probs[i]:.2f} \\\\\n"
        tex += "\\bottomrule\\end{tabular}\\end{table}\n"
        tex += f"Terpilih Parent 1: {parents[0]}\\\\\n"
        tex += f"Terpilih Parent 2: {parents[1]}\n"
        
        tex += "\\vspace{0.5cm}\\textbf{3. Crossover (Order Crossover / OX)}\\\\"
        tex += "Menghasilkan keturunan menggunakan probabilitas crossover $P_c = 0.8$.\\\\\n"
        new_population = []
        best_curr = sorted_pop[0]
        new_population.append(best_curr)
        tex += f"\\textbf{{Elitism diterapkan}}: Kromosom terbaik diteruskan tanpa diubah: {best_curr}\\\\\n"
        
        while len(new_population) < POP_SIZE:
            r_cross = random.random()
            if r_cross <= PC:
                child, s, e = order_crossover(parents[0], parents[1])
                tex += f"\\textbullet\\ $r\\_cross = {r_cross:.2f} \\le 0.8$: Crossover pada titik {s} hingga {e}.\\\\ Anak dihasilkan: {child}\\\\\n"
                new_population.append(child)
            else:
                tex += f"\\textbullet\\ $r\\_cross = {r_cross:.2f} > 0.8$: Tidak terjadi crossover. Anak menyalin Parent 1.\\\\\n"
                new_population.append(parents[0])
                
        tex += "\\vspace{0.5cm}\\textbf{4. Mutasi (Inversion Mutation)}\\\\"
        tex += "Mengecek kromosom baru (kecuali individu elit) untuk mutasi dengan $P_m = 0.2$.\\\\\n"
        for i in range(1, POP_SIZE):
            r_mut = random.random()
            if r_mut <= PM:
                mutated, s, e = inversion_mutation(new_population[i])
                tex += f"\\textbullet\\ Anak {i+1} ($r\\_mut = {r_mut:.2f} \\le 0.2$): Mutasi inversi segmen dari titik {s} hingga {e}.\\\\ Hasil: {mutated}\\\\\n"
                new_population[i] = mutated
            else:
                tex += f"\\textbullet\\ Anak {i+1} ($r\\_mut = {r_mut:.2f} > 0.2$): Tidak terjadi mutasi.\\\\\n"
        
        population = new_population
        tex += "\\vspace{1cm}\n"
        
    tex += "\\section{Kesimpulan}\n"
    tex += "Setelah 5 iterasi Algoritma Genetika dengan Elitism, performa program terpusat pada solusi kromosom elitnya akibat sifat konvergensi Rank Selection di populasi kecil.\n\n"
    tex += f"\\textbf{{Total Jarak Terpendek Terbaik:}} {best_overall_dist:.2f}\\\\\n"
    tex += f"\\textbf{{Representasi Kromosom (Rute Terbaik):}} {best_overall_route}\\\\\n"
    
    route_str = " $\\rightarrow$ ".join([cities[i][0] for i in best_overall_route])
    tex += f"\\textbf{{Rute Kota:}} {route_str}\n"

    tex += r"""
\end{document}
"""
    with open("report.tex", "w", encoding='utf-8') as f:
        f.write(tex)

if __name__ == "__main__":
    create_latex()
