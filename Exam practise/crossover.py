# Crossover (Single point crossover)
def crossover(parent1, parent2):
point = random.randint(0, num_shifts - 1)
child = [parent1[i][:point] + parent2[i][point:] for i in
range(num_staff)]
return child