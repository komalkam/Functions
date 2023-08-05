from collections import defaultdict, deque

class Tree:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_nodes_at_level(self, start_node, target_level):
        visited = set()
        queue = deque([(start_node, 0)])  # Tuple format: (node, level)
        count = 0

        while queue:
            current_node, current_level = queue.popleft()

            if current_level == target_level:
                count += 1

            visited.add(current_node)

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, current_level + 1))

        return count


t = Tree()
t.add_edge(0, 1)
t.add_edge(0, 2)
t.add_edge(1, 3)
t.add_edge(1, 4)
t.add_edge(2, 5)
t.add_edge(2, 6)

target_level = 2
start_node = 0

count = t.count_nodes_at_level(start_node, target_level)
print(f"Number of nodes at level {target_level}: {count}")
