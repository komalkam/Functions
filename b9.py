from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    max_sum = float('-inf')
    max_sum_level = 0

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.key

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_level += 1

    return max_sum_level


if __name__ == "__main__":
   
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)


    max_sum_level = max_level_sum(root)
    print("Level with maximum sum in the binary tree:", max_sum_level)
