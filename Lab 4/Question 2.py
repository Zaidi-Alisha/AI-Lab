import heapq
import random
import time
from collections import defaultdict

class DynamicGraph:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.edge_costs = defaultdict(dict)
        self.initialize_edge_costs()
        self.last_update_time = time.time()
        self.update_interval = 1.0  

    def initialize_edge_costs(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #right, down, left, up
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == '#':
                    continue  #to skip walls
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.rows and 0 <= nj < self.cols and self.grid[ni][nj] != '#':
                        self.edge_costs[(i, j)][(ni, nj)] = 1

    def update_edge_costs_randomly(self):
        current_time = time.time()
        if current_time - self.last_update_time < self.update_interval:
            return False
        
        self.last_update_time = current_time
        changed_edges = []
      
        all_edges = []
        for u in self.edge_costs:
            for v in self.edge_costs[u]:
                all_edges.append((u, v))
        
        num_to_change = max(1, int(0.2 * len(all_edges)))
        edges_to_change = random.sample(all_edges, num_to_change)
        
        for u, v in edges_to_change:
            new_cost = random.randint(1, 10)
            old_cost = self.edge_costs[u][v]
            if new_cost != old_cost:
                self.edge_costs[u][v] = new_cost
                self.edge_costs[v][u] = new_cost 
                changed_edges.append((u, v, old_cost, new_cost))
        
        return changed_edges

    def get_neighbors(self, node):
        return [(n, cost) for n, cost in self.edge_costs.get(node, {}).items()]

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

class DynamicAStar:
    def __init__(self, graph):
        self.graph = graph
        self.open_set = []
        self.came_from = {}
        self.g_score = defaultdict(lambda: float('inf'))
        self.f_score = defaultdict(lambda: float('inf'))
        self.in_open_set = set()
        self.changed_edges = []
        self.current_path = []
        self.last_recompute_time = 0

    def initialize_search(self, start, goal):
        self.open_set = []
        self.came_from = {}
        self.g_score = defaultdict(lambda: float('inf'))
        self.f_score = defaultdict(lambda: float('inf'))
        self.in_open_set = set()
        
        self.g_score[start] = 0
        self.f_score[start] = self.graph.heuristic(start, goal)
        heapq.heappush(self.open_set, (self.f_score[start], start))
        self.in_open_set.add(start)

    def reconstruct_path(self, current):
        path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            path.append(current)
        return path[::-1]

    def adapt_to_changes(self, start, goal, changed_edges):
        affected_nodes = set()
        
        for u, v, old_cost, new_cost in changed_edges:
            if self.g_score[v] > self.g_score[u] + new_cost:
                affected_nodes.add(v)
            if self.g_score[u] > self.g_score[v] + new_cost:
                affected_nodes.add(u)
        
        for node in affected_nodes:
            if node in self.in_open_set:
                for i, (f, n) in enumerate(self.open_set):
                    if n == node:
                        self.open_set[i] = (self.f_score[node], node)
                        heapq.heapify(self.open_set)
                        break
            else:
                heapq.heappush(self.open_set, (self.f_score[node], node))
                self.in_open_set.add(node)

    def find_path(self, start, goal, max_iterations=10000):
        self.initialize_search(start, goal)
        
        for iteration in range(max_iterations):
            changed_edges = self.graph.update_edge_costs_randomly()
            if changed_edges:
                self.adapt_to_changes(start, goal, changed_edges)
            
            if not self.open_set:
                return None  
            
            current_f, current = heapq.heappop(self.open_set)
            self.in_open_set.remove(current)
            
            if current == goal:
                self.current_path = self.reconstruct_path(current)
                return self.current_path
            
            for neighbor, cost in self.graph.get_neighbors(current):
                tentative_g_score = self.g_score[current] + cost
                
                if tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = tentative_g_score + self.graph.heuristic(neighbor, goal)
                    
                    if neighbor not in self.in_open_set:
                        heapq.heappush(self.open_set, (self.f_score[neighbor], neighbor))
                        self.in_open_set.add(neighbor)
            
            if iteration % 100 == 0 and self.came_from:
                self.current_path = self.reconstruct_path(current)
        
        return None  

if __name__ == "__main__":
    grid = [
        ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['#', '#', ' ', '#', ' ', '#', ' ', ' '],
        [' ', ' ', ' ', '#', ' ', '#', ' ', ' '],
        [' ', '#', '#', '#', ' ', '#', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '#', '#', '#', '#', '#', ' ', '#'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G']
    ]
    
    graph = DynamicGraph(grid)
    astar = DynamicAStar(graph)
    
    start = None
    goal = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
    
    if start and goal:
        print("Starting dynamic A* search...")
        path = astar.find_path(start, goal)
        
        if path:
            print(f"Found path with cost {astar.g_score[goal]}:")
            for step in path:
                print(step)
            
            grid_vis = [row.copy() for row in grid]
            for i, (x, y) in enumerate(path[1:-1]):  
                if grid_vis[x][y] == ' ':
                    grid_vis[x][y] = '.'
            
            print("\nPath visualization:")
            for row in grid_vis:
                print(' '.join(row))
        else:
            print("No path found or max iterations reached")
    else:
        print("Start or goal not found in grid")
