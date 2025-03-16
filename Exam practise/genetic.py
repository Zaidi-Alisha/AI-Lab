import random

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def fitness(binary_str):
    x = binary_to_decimal(binary_str)
    return 2 * (x ** 2) - 1

def generate_population(size=10):
    return [''.join(random.choice('01') for _ in range(6)) for _ in range(size)]

def tournament_selection(population, k=3):
    return max(random.sample(population, k), key=fitness)

def uniform_crossover(parent1, parent2):
    return ''.join(random.choice([p1, p2]) for p1, p2 in zip(parent1, parent2))

def mutate(binary_str, mutation_rate=0.1):
    return ''.join(bit if random.random() > mutation_rate else str(1 - int(bit)) for bit in binary_str)

def genetic_algorithm(generations=50, population_size=10):
    population = generate_population(population_size)
    
    for _ in range(generations):
        new_population = []
        for _ in range(len(population) // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1 = uniform_crossover(parent1, parent2)
            child2 = uniform_crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population

    return max(population, key=fitness)

best_solution = genetic_algorithm()
print(f"Best solution: {best_solution} with x = {binary_to_decimal(best_solution)}, f(x) = {fitness(best_solution)}")
