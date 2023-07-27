def is_operator(char):
    return char in "+-*/"

def prefix_to_infix(prefix_expression):
    stack = []
    for char in reversed(prefix_expression):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expression = f"({operand1} {char} {operand2})"
            stack.append(infix_expression)
        else:
            stack.append(char)
    
    return stack[0]

# Test the function
if __name__ == "__main__":
    prefix_expr = input("Enter the prefix expression: ")
    infix_expr = prefix_to_infix(prefix_expr)
    print("Infix Expression:", infix_expr)
