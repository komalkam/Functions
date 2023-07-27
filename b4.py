class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_leaves(root):
    if not root:
        return

    if not root.left and not root.right:
        print(root.key, end=" ")  

    print_leaves(root.left)      
    print_leaves(root.right)     


if __name__ == "__main__":
   
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)

 
    print("Leaves in the binary tree:", end=" ")
    print_leaves(root)
