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

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current_node, result):
        if current_node:
            self._inorder_traversal_recursive(current_node.left, result)
            result.append(current_node.key)
            self._inorder_traversal_recursive(current_node.right, result)


if __name__ == "__main__":
    binary_tree = BinaryTree()

  
    elements = input("Enter the elements of the binary tree (space-separated): ").split()
    elements = list(map(int, elements))

    for element in elements:
        binary_tree.insert(element)

    sorted_elements = binary_tree.inorder_traversal()
    print("Inorder Traversal of Binary Tree:", sorted_elements)
