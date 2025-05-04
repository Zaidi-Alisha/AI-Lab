import random

# Configurations
string_length = 20
population_size = 50
num_generations = 50
top_k = 10  # number of individuals selected for estimation

# Fitness: Number of 1s in the string
def fitness(individual):
    return sum(individual)

# Generate random binary individual
def random_individual(length):
    return [random.randint(0, 1) for _ in range(length)]

# Generate initial population
def generate_population(size, length):
    return [random_individual(length) for _ in range(size)]

# Estimate distribution (probability of 1 at each position)
def estimate_distribution(selected_individuals):
    length = len(selected_individuals[0])
    probabilities = []
    for i in range(length):
        prob_1 = sum(ind[i] for ind in selected_individuals) / len(selected_individuals)
        probabilities.append(prob_1)
    return probabilities

# Sample new individuals based on estimated probabilities
def sample_new_population(probabilities, size):
    new_population = []
    for _ in range(size):
        individual = [1 if random.random() < prob else 0 for prob in probabilities]
        new_population.append(individual)
    return new_population

# EDA main loop
population = generate_population(population_size, string_length)

for generation in range(num_generations):
    # Evaluate fitness of population
    population.sort(key=fitness, reverse=True)
    best_fitness = fitness(population[0])
    print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    # Select top individuals
    selected = population[:top_k]

    # Estimate distribution and sample new individuals
    probabilities = estimate_distribution(selected)
    population = sample_new_population(probabilities, population_size)

# Final output
print("\nBest individual found:")
print(population[0])
print("Fitness:", fitness(population[0]))
