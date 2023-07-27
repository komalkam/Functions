class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def perfect_binary_tree_sum(height):
    return (2**(height + 1)) - 1


if __name__ == "__main__":
    height = 3  

   
    total_sum = perfect_binary_tree_sum(height)
    print("Sum of all nodes in the perfect binary tree:", total_sum)
