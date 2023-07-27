def are_brackets_closed(code_snippet):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in code_snippet:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or brackets_map[char] != stack.pop():
                return False

    return not stack

# Test the function
if __name__ == "__main__":
    code_snippet = input("Enter the code snippet: ")
    if are_brackets_closed(code_snippet):
        print("All brackets are closed.")
    else:
        print("Not all brackets are closed.")
