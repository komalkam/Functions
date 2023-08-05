from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic(self):
        visited = set()
        rec_stack = set()

        for node in self.graph:
            if self.dfs(node, visited, rec_stack):
                return True

        return False

    def dfs(self, node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False


g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(4, 5)

if g.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
