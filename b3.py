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

    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result

    def _preorder_traversal_recursive(self, current_node, result):
        if current_node:
            result.append(current_node.key)
            self._preorder_traversal_recursive(current_node.left, result)
            self._preorder_traversal_recursive(current_node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current_node, result):
        if current_node:
            self._inorder_traversal_recursive(current_node.left, result)
            result.append(current_node.key)
            self._inorder_traversal_recursive(current_node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result

    def _postorder_traversal_recursive(self, current_node, result):
        if current_node:
            self._postorder_traversal_recursive(current_node.left, result)
            self._postorder_traversal_recursive(current_node.right, result)
            result.append(current_node.key)


if __name__ == "__main__":
    binary_tree = BinaryTree()

    
    elements = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    
    for element in elements:
        binary_tree.insert(element)

    preorder_result = binary_tree.preorder_traversal()
    print("Pre-order Traversal:", preorder_result)

    inorder_result = binary_tree.inorder_traversal()
    print("In-order Traversal:", inorder_result)

    postorder_result = binary_tree.postorder_traversal()
    print("Post-order Traversal:", postorder_result)
