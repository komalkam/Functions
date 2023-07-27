class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left:
                self._insert_recursive(current_node.left, key)
            else:
                current_node.left = Node(key)
        else:
            if current_node.right:
                self._insert_recursive(current_node.right, key)
            else:
                current_node.right = Node(key)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current_node):
        if not current_node:
            return -1

        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)

        return 1 + max(left_height, right_height)

if __name__ == "__main__":
    binary_tree = BinaryTree()

    
    elements = input("Enter the elements of the binary tree (space-separated): ").split()
    elements = list(map(int, elements))

    for element in elements:
        binary_tree.insert(element)

    tree_height = binary_tree.height()
    print("Height of the Binary Tree:", tree_height)
