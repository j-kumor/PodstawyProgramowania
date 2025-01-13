def calculate_rpn(expression):
    # Initialize an empty stack
    stack = []
    
    # Split the input expression into tokens (numbers and operators)
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  # If token is a number
            stack.append(int(token))
        elif token in '+-*/':  # If token is an operator
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        elif token == '=':  # If token is '=', print the result
            result = stack.pop()
            print(f"Result: {result}")
        else:
            print("Invalid token encountered.")
            return

# Main program loop to enter expressions
while True:
    expression = input("Enter an RPN expression (e.g., 2 3 + =): ")
    if expression.lower() == 'quit':
        print("Exiting the program.")
        break
    else:
        calculate_rpn(expression)
