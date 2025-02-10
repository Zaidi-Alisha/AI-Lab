def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    min_cost = float("inf")
    best_path = []
    def find_permutations(path, remaining, cost):
        nonlocal min_cost, best_path
        if not remaining:
            cost += graph[path[-1]][start]
            if cost < min_cost:
                min_cost = cost
                best_path = path + [start]
            return
        for city in remaining:
            find_permutations(path + [city], [c for c in remaining if c != city], cost + graph[path[-1]][city])
    
    find_permutations([start], nodes, 0)
    return best_path, min_cost

graph_tsp = {
    'A': {'B': 13, 'C': 5, 'D': 11},
    'B': {'A': 9, 'C': 19, 'D': 17},
    'C': {'A': 7, 'B': 12, 'D': 6},
    'D': {'A': 16, 'B': 8, 'C': 10}
}

start_city = 'A'
print(tsp(graph_tsp, start_city))