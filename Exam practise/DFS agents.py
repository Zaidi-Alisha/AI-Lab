def dfs(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == target:
            return path  # Return a valid path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 'X' and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))
    
    return None  # No path found

print(dfs(grid, start, target))
