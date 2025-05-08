import heapq
from collections import deque

def solve_maze_multiple_goals(maze):
    start = None
    goals = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goals.append((i, j))
    
    if not start or not goals:
        return None
      
    important_points = [start] + goals
    n = len(important_points)
    
    #find pairwise shortest path
    distance_matrix = [[0]*n for _ in range(n)]
    paths = {}
    
    for i in range(n):
        for j in range(i+1, n):
            path = bfs_shortest_path(maze, important_points[i], important_points[j])
            if not path:
                return None  # maze is unsolvable
            distance_matrix[i][j] = distance_matrix[j][i] = len(path) - 1
            paths[(i, j)] = path
            paths[(j, i)] = path[::-1]
    
    #heuristic approach will be used
    best_order = greedy_tsp_heuristic(distance_matrix)
    
    #find path by making a path between points
    full_path = []
    for i in range(len(best_order)-1):
        from_idx = best_order[i]
        to_idx = best_order[i+1]
        segment = paths[(from_idx, to_idx)]
        if i > 0:
            segment = segment[1:]  #no duplicate points
        full_path.extend(segment)
    
    return full_path

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque()
    queue.append((start[0], start[1], [start]))
    
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, path = queue.popleft()
        
        if (x, y) == end:
            return path
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < rows and 0 <= ny < cols and 
                maze[nx][ny] != '#' and 
                (nx, ny) not in visited):
                
                visited.add((nx, ny))
                new_path = path + [(nx, ny)]
                queue.append((nx, ny, new_path))
    
    return None 

def greedy_tsp_heuristic(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(1, n)) 
    current = 0
    order = [current]
    
    while unvisited:
        nearest = min(unvisited, key=lambda x: distance_matrix[current][x])
        order.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    
    return order
if __name__ == "__main__":
    maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', 'S', ' ', ' ', '#', ' ', ' ', ' ', 'G', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', 'G', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    
    path = solve_maze_multiple_goals(maze)
    if path:
        print("Path found with length:", len(path)-1)
        print("Path:", path)
        
        # Visualize the path in the maze
        maze_with_path = [row.copy() for row in maze]
        for i, (x, y) in enumerate(path[1:-1]):
            if maze_with_path[x][y] == ' ':
                maze_with_path[x][y] = '.'
        
        print("\nMaze with path:")
        for row in maze_with_path:
            print(' '.join(row))
    else:
        print("No path found that visits all goals")
