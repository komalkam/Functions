from collections import defaultdict

class Forest:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_trees(self):
        visited = set()
        trees = 0

        for node in self.graph:
            if node not in visited:
                self.dfs(node, visited)
                trees += 1

        return trees

    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


f = Forest()
f.add_edge(0, 1)
f.add_edge(0, 2)
f.add_edge(3, 4)
f.add_edge(5, 6)

tree_count = f.count_trees()
print(f"Number of trees in the forest: {tree_count}")
