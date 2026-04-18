import csv
import math
import random
import sys

# Constants for GA
POP_SIZE = 4
ITERATIONS = 5
PC = 0.8  # Crossover Probability
PM = 0.2  # Mutation Probability
SEED = 42

random.seed(SEED)

def euclidean_distance(city1, city2):
    return math.sqrt((city1[1] - city2[1])**2 + (city1[2] - city2[2])**2)

def calculate_route_distance(route, dist_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += dist_matrix[route[i]][route[i+1]]
    total += dist_matrix[route[-1]][route[0]] # return to start
    return total

def rank_selection(population, fitness):
    # Sort population by fitness (descending)
    sorted_pop = [x for _, x in sorted(zip(fitness, population), reverse=True)]
    n = len(sorted_pop)
    ranks = list(range(1, n + 1))
    # Ranks are assigned such that the best gets rank N, worst gets rank 1
    # since we zip(fitness, ...), the first is the best, so reverse rank assignment
    rank_probs = [rank / sum(ranks) for rank in reversed(ranks)]
    
    # Cumulative probabilities
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
    start, end = min(c1, c2), max(c1, c2)
    
    child = [-1] * n
    # Copy from p1
    child[start:end+1] = p1[start:end+1]
    
    # Fill from p2
    p2_idx = (end + 1) % n
    child_idx = (end + 1) % n
    
    while -1 in child:
        if p2[p2_idx] not in child:
            child[child_idx] = p2[p2_idx]
            child_idx = (child_idx + 1) % n
        p2_idx = (p2_idx + 1) % n
        
    return child, start, end

def inversion_mutation(ind):
    n = len(ind)
    c1, c2 = random.sample(range(n), 2)
    start, end = min(c1, c2), max(c1, c2)
    
    mutated = ind[:]
    mutated[start:end+1] = reversed(mutated[start:end+1])
    return mutated, start, end

def main():
    cities = [
        ("Denver",39.7420,-104.9915),
        ("Colorado Springs",38.8461,-104.8006),
        ("Telluride",37.9375,-107.8123),
        ("Las Vegas",36.1146,-115.1728),
        ("Grand Canyon",36.0565,-112.1251),
        ("Yellowstone National Park",44.4237,-110.5885),
        ("Mount Rushmore",43.9686,-103.3818),
        ("Seattle",47.6080,-122.3352),
        ("Redwood National Park",41.2131,-124.0046),
        ("San Diego",32.7157,-117.1610),
        ("Los Angeles",34.05223,-118.24368),
        ("Mount Hood National Forest",45.454350,-121.933136),
        ("Santa Fe",35.691544,-105.944183),
        ("Chicago",41.881832,-87.623177),
        ("New York City",40.730610,-73.935242)
    ]
    
    n_cities = len(cities)
    dist_matrix = [[0]*n_cities for _ in range(n_cities)]
    for i in range(n_cities):
        for j in range(n_cities):
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            
    # Initialization
    population = [list(range(n_cities)) for _ in range(POP_SIZE)]
    for p in population:
        random.shuffle(p)
        
    best_overall_dist = float('inf')
    best_overall_route = []
    
    # Store complete log for manual generation
    with open('ga_manual_trace.txt', 'w') as f:
        for it in range(ITERATIONS):
            f.write(f"=== ITERASI {it+1} ===\n")
            
            # 1. Hitung Fitness
            distances = [calculate_route_distance(p, dist_matrix) for p in population]
            fitness = [1/d for d in distances]
            f.write("1. Evaluasi Fitness:\n")
            for i, (p, d, fit) in enumerate(zip(population, distances, fitness)):
                f.write(f"Kromosom {i+1}: {p} | Jarak: {d:.2f} | Fitness: {fit:.6f}\n")
                
            best_idx = distances.index(min(distances))
            if distances[best_idx] < best_overall_dist:
                best_overall_dist = distances[best_idx]
                best_overall_route = population[best_idx][:]
                
            f.write(f"\n2. Rank Selection:\n")
            parents, sorted_pop, rank_probs, cum_probs = rank_selection(population, fitness)
            for i, sp in enumerate(sorted_pop):
                f.write(f"Rank {len(sorted_pop)-i}: {sp} | Prob: {rank_probs[i]:.2f} | CumProb: {cum_probs[i]:.2f}\n")
            f.write(f"Terpilih sebagai Parent 1: {parents[0]}\n")
            f.write(f"Terpilih sebagai Parent 2: {parents[1]}\n")
            
            f.write(f"\n3. Crossover (Order Crossover / OX) (prob = {PC}):\n")
            new_population = []
            
            # Elitism: keep best
            best_curr = sorted_pop[0]
            new_population.append(best_curr)
            f.write(f"** Elitism (Kromosom Terbaik diteruskan): {best_curr}\n")
            
            # Generate offspring
            while len(new_population) < POP_SIZE:
                r_cross = random.random()
                f.write(f"Random value for crossover (r_cross): {r_cross:.2f}\n")
                if r_cross <= PC:
                    child, s, e = order_crossover(parents[0], parents[1])
                    f.write(f"  Crosover pada titik {s} s/d {e}\n")
                    f.write(f"  Anak dihasilkan: {child}\n")
                    new_population.append(child)
                else:
                    f.write("  Tidak terjadi crossover, salin parent.\n")
                    new_population.append(parents[0])
                    
            f.write(f"\n4. Mutation (Inversion Mutation) (prob = {PM}):\n")
            for i in range(1, POP_SIZE):  # Skip elite
                r_mut = random.random()
                f.write(f"Kromosom baru {i+1}: Random r_mut = {r_mut:.2f}\n")
                if r_mut <= PM:
                    mutated, s, e = inversion_mutation(new_population[i])
                    f.write(f"  Mutasi pada titik {s} s/d {e}\n")
                    f.write(f"  Hasil mutasi: {mutated}\n")
                    new_population[i] = mutated
                    
            population = new_population
            f.write("\n")
            
        f.write("=== KESIMPULAN ===\n")
        f.write(f"Jarak terbaik ditemukan: {best_overall_dist:.2f}\n")
        f.write(f"Rute terbaik: {best_overall_route}\n")
        f.write("Kota rute: " + " -> ".join([cities[i][0] for i in best_overall_route]))

if __name__ == '__main__':
    main()
