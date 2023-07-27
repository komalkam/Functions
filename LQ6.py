def is_operator(char):
    return char in "+-*/"

def postfix_to_prefix(postfix_expression):
    stack = []
    for char in postfix_expression:
        if is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = char + operand1 + operand2
            stack.append(prefix_expression)
        else:
            stack.append(char)
    
    return stack[0]

# Test the function
if __name__ == "__main__":
    postfix_expr = input("Enter the postfix expression: ")
    prefix_expr = postfix_to_prefix(postfix_expr)
    print("Prefix Expression:", prefix_expr)
