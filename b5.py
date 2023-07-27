from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue.extend(self.graph[node])

        return result

    def dfs(self, start_node):
        visited = set()
        result = []

        def dfs_recursive(node):
            visited.add(node)
            result.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)
        return result

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    start_node = 2

    print("BFS Traversal:", graph.bfs(start_node))
    print("DFS Traversal:", graph.dfs(start_node))
