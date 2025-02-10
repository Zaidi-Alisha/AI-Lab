class GoalBasedAgentDFS:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        return "Goal reached" if percept == self.goal else "Searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return f"Goal {self.goal} found!"
        return environment.dfs_search(percept, self.goal)

class EnvironmentDFS:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dfs_search(self, start, goal):
        visited = []
        stack = [start]
        while stack:
            node = stack.pop()
            print(f"Visiting: {node}")
            if node == goal:
                return f"Goal {goal} found"
            if node not in visited:
                visited.append(node)
                stack.extend(reversed(self.graph.get(node, [])))
        return "Was unable to find goal"

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    print(agent.act(percept, environment))

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

start_node = 'A'
goal_node = 'I'
agent_dfs = GoalBasedAgentDFS(goal_node)
environment_dfs = EnvironmentDFS(graph)
run_agent(agent_dfs, environment_dfs, start_node)