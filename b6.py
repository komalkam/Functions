class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if not root:
        return 0

    sum_left = 0

    if root.left and not root.left.left and not root.left.right:
        sum_left += root.left.key

    sum_left += sum_of_left_leaves(root.left)
    sum_left += sum_of_left_leaves(root.right)

    return sum_left

if __name__ == "__main__":
   
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)


    print("Sum of left leaves in the binary tree:", sum_of_left_leaves(root))
