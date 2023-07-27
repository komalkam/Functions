class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def count_subtrees_with_sum_x(root, x):
    def count_subtrees_with_sum_x_recursive(node, x, count):
        if not node:
            return 0

        left_sum = count_subtrees_with_sum_x_recursive(node.left, x, count)
        right_sum = count_subtrees_with_sum_x_recursive(node.right, x, count)

        current_sum = left_sum + right_sum + node.key

        if current_sum == x:
            count[0] += 1

        return current_sum

    count = [0]  
    count_subtrees_with_sum_x_recursive(root, x, count)
    return count[0]

if __name__ == "__main__":
   
    root = Node(5)
    root.left = Node(-10)
    root.right = Node(3)
    root.left.left = Node(9)
    root.left.right = Node(8)
    root.right.left = Node(-4)
    root.right.right = Node(7)

    x = 7  

    
    count = count_subtrees_with_sum_x(root, x)
    print("Number of subtrees that sum up to", x, ":", count)
