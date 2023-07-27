class Stack:
    def __init__(self):
        self.items = []
        self.min_value = None

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.is_empty() or item < self.min_value:
            self.min_value = item
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def get_min(self):
        return self.min_value


if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(2)
    stack.push(6)
    stack.push(1)
    stack.push(5)

    print("Smallest number in the stack:", stack.get_min())
