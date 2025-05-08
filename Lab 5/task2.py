import math
import random

# Euclidean distance between two points
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Total distance of the route
def total_distance(route):
    dist = 0
    for i in range(len(route)):
        dist += distance(route[i], route[(i + 1) % len(route)])  # return to start
    return dist

# Generate a neighboring route by swapping two cities
def get_neighbor(route):
    neighbor = route.copy()
    i, j = random.sample(range(len(route)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

# Hill Climbing Algorithm
def hill_climb(locations, max_iterations=1000):
    current_route = locations[:]
    random.shuffle(current_route)
    current_distance = total_distance(current_route)

    for _ in range(max_iterations):
        neighbor = get_neighbor(current_route)
        neighbor_distance = total_distance(neighbor)
        
        # Accept the neighbor only if it improves the distance
        if neighbor_distance < current_distance:
            current_route = neighbor
            current_distance = neighbor_distance

    return current_route, current_distance

# Example: Delivery point coordinates
locations = [
    (0, 0),
    (2, 3),
    (5, 2),
    (6, 6),
    (8, 3),
    (1, 7)
]

# Run the algorithm
best_route, best_distance = hill_climb(locations)

# Print results
print("Optimized Route:")
for point in best_route:
    print(point)
print("\nTotal Distance:", round(best_distance, 2))
