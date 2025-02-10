graph = {
    'A': ['B', 'D', 'H'],
    'B': ['D', 'E'],
    'C': ['G', 'I'],
    'D': ['E', 'H'],
    'E': ['B', 'H', 'G'],
    'F': ['I'],
    'G': ['A', 'B', 'C'],
    'H': ['C'],
    'I': ['G']
}

#iterative deepening search
def iterative_deepening(start, goal, max_depth):
    for depth in range(max_depth + 1):
        result = dls_search(start, goal, depth)
        if "found" in result:
            return result
    return "Unable to find goal within depth limit"

def dls_search(node, goal, depth_limit, depth=0):
    if depth > depth_limit:
        return ""
    if node == goal:
        return f"Goal {goal} found"
    for neighbor in graph.get(node, []):
        result = dls_search(neighbor, goal, depth_limit, depth + 1)
        if result:
            return result
    return ""

start_node = 'A'
goal_node = 'I'
max_search_depth = 5
print(iterative_deepening(start_node, goal_node, max_search_depth))

#bidirectional search
from collections import deque

def bidirectional_search(graph, start, goal):
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start}
    backward_visited = {goal}

    while forward_queue and backward_queue:
        if forward_queue:
            node = forward_queue.popleft()
            if node in backward_visited:
                return "Goal found by using bidirectional search"
            forward_visited.add(node)
            forward_queue.extend(n for n in graph.get(node, []) if n not in forward_visited)
        
        if backward_queue:
            node = backward_queue.popleft()
            if node in forward_visited:
                return "Goal found using bidirectional search"
            backward_visited.add(node)
            backward_queue.extend(n for n in graph.get(node, []) if n not in backward_visited)
    
    return "Was unable to find goal"

print(bidirectional_search(graph, 'A', 'I'))
