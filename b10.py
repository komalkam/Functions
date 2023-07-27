from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_nodes_at_odd_levels(root):
    if not root:
        return

    queue = deque()
    queue.append((root, 1)) 

    while queue:
        node, level = queue.popleft()

        if level % 2 != 0:
            print(node.key, end=" ")

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))


if __name__ == "__main__":
   
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)


    print("Nodes at odd levels:", end=" ")
    print_nodes_at_odd_levels(root)
