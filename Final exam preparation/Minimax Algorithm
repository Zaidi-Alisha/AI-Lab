import math

# Node class to construct game tree
class Node:
    def __init__(self, value=None):
        self.value = value            # Heuristic value if it's a leaf node
        self.children = []           # List of child nodes
        self.minmax_value = None     # Value determined by minimax algorithm

# Agent using Minimax strategy
class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            return environment.compute_minimax(node, self.depth)

# Environment that simulates the game tree
class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    # Recursive minimax computation
    def compute_minimax(self, node, depth, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, False)
                value = max(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, True)
                value = min(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value

# Function to run the agent
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)

# ---- MAIN ----
# Build a sample game tree
root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n3.children = [Node(2), Node(3)]
n4.children = [Node(5), Node(9)]
n5.children = [Node(0), Node(1)]
n6.children = [Node(7), Node(5)]

depth = 3

# Instantiate Agent and Environment
agent = MinimaxAgent(depth)
environment = Environment(root)

# Run Minimax Agent
run_agent(agent, environment, root)

# Print Results
print("Computed Nodes (in order):", environment.computed_nodes)
print("Minimax values at key nodes:")
print(f"A: {root.minmax_value}")
print(f"B: {n1.minmax_value}")
print(f"C: {n2.minmax_value}")
