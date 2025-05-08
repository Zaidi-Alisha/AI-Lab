import random
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the cities and distances between them
cities = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
num_cities = len(cities)

# Randomly generate distances between cities
# This is a symmetric distance matrix where distance[i][j] == distance[j][i]
np.random.seed(42)
distance_matrix = np.random.randint(10, 100, size=(num_cities, num_cities))
for i in range(num_cities):
    distance_matrix[i, i] = 0  # No distance to itself

# Step 2: Define the fitness function to evaluate a tour's total distance
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i], tour[i+1]]
    total_distance += distance_matrix[tour[-1], tour[0]]  # Return to the starting city
    return total_distance

# Step 3: Generate a random population of tours
def create_initial_population(pop_size):
    population = []
    for _ in range(pop_size):
        tour = list(range(num_cities))
        random.shuffle(tour)
        population.append(tour)
    return population

# Step 4: Select parents using tournament selection
def tournament_selection(population, tournament_size=5):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda tour: calculate_total_distance(tour))
    return tournament[0], tournament[1]

# Step 5: Implement the ordered crossover operator
def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(num_cities), 2))  # Randomly choose crossover points
    
    # Copy the middle part from parent1
    child = [-1] * num_cities
    child[start:end+1] = parent1[start:end+1]
    
    # Fill the remaining spots from parent2
    fill_idx = 0
    for i in range(num_cities):
        if child[i] == -1:
            while parent2[fill_idx] in child:
                fill_idx += 1
            child[i] = parent2[fill_idx]
    
    return child

# Step 6: Implement mutation by swapping two cities in a tour
def mutate(tour, mutation_rate=0.05):
    if random.random() < mutation_rate:
        i, j = random.sample(range(num_cities), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Step 7: Main genetic algorithm loop
def genetic_algorithm(pop_size=100, generations=500, mutation_rate=0.05):
    # Initialize the population
    population = create_initial_population(pop_size)
    
    best_tour = None
    best_distance = float('inf')
    
    for gen in range(generations):
        # Evaluate fitness
        population.sort(key=lambda tour: calculate_total_distance(tour))
        
        # Keep track of the best tour found so far
        if calculate_total_distance(population[0]) < best_distance:
            best_tour = population[0]
            best_distance = calculate_total_distance(population[0])
        
        # Create a new population using selection, crossover, and mutation
        new_population = []
        
        while len(new_population) < pop_size:
            parent1, parent2 = tournament_selection(population)
            child = ordered_crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
        
        # Print the best solution of each generation
        if gen % 50 == 0:
            print(f"Generation {gen}: Best Distance = {best_distance}")
    
    return best_tour, best_distance

# Step 8: Run the genetic algorithm
best_tour, best_distance = genetic_algorithm()

# Step 9: Output the best solution
print("\nBest Tour:", [cities[i] for i in best_tour])
print("Best Distance:", best_distance)

# Step 10: Plot the path of the best tour
def plot_tsp_solution(best_tour):
    x = np.random.rand(num_cities)
    y = np.random.rand(num_cities)
    
    plt.figure(figsize=(10, 8))
    for i in range(num_cities):
        plt.scatter(x[i], y[i], label=cities[i])
        plt.text(x[i] + 0.01, y[i] + 0.01, cities[i], fontsize=12)
    
    for i in range(num_cities):
        plt.plot([x[best_tour[i]], x[best_tour[(i + 1) % num_cities]]], 
                 [y[best_tour[i]], y[best_tour[(i + 1) % num_cities]]], 'k-', lw=2)
    
    plt.title("Best TSP Solution")
    plt.show()

# Plot the best solution
plot_tsp_solution(best_tour)
