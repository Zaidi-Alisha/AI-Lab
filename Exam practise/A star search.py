import heapq

def a_star(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    def heuristic(a, b):  # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_set = [(0 + heuristic(start, target), 0, start, [])]  # (f, g, position, path)
    visited = set()

    while open_set:
        _, cost, (x, y), path = heapq.heappop(open_set)

        if (x, y) == target:
            return path + [(x, y)]  # Return the optimal path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                new_cost = cost + grid[nx][ny]
                heapq.heappush(open_set, (new_cost + heuristic((nx, ny), target), new_cost, (nx, ny), path + [(x, y)]))
    
    return None  # No path found

# Example usage:
grid = [
    [1, 2, 3, '#', 4],
    [1, '#', 1, 2, 2],
    [2, 3, 1, '#', 1],
    ['#', '#', 2, 1, 1],
    [1, 1, 2, 2, 1]
]
start = (0, 0)
target = (4, 4)
print(a_star(grid, start, target))
