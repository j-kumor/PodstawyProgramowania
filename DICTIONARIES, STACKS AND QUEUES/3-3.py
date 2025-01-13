import queue

# Function to check if the brackets are correctly balanced
def brackets_ok(expression):
    # Create a stack using LifoQueue
    stack = queue.LifoQueue()

    # Define a dictionary for matching pairs of brackets
    matching_brackets = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the expression
    for char in expression:
        if char in "({[":
            # If the character is an opening bracket, push it onto the stack
            stack.put(char)
        elif char in ")}]":
            # If the character is a closing bracket, check for matching opening bracket
            if stack.empty():
                return False  # Stack is empty, but there is a closing bracket
            top = stack.get()
            if top != matching_brackets[char]:
                return False  # Mismatched brackets

    # If the stack is empty, all brackets matched correctly
    return stack.empty()

# Test expressions
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

# Check correctness of each expression
if brackets_ok(expression1):
    print("Expression 1: Brackets are correct.")
else:
    print("Expression 1: Brackets are not correct.")

if brackets_ok(expression2):
    print("Expression 2: Brackets are correct.")
else:
    print("Expression 2: Brackets are not correct.")

if brackets_ok(expression3):
    print("Expression 3: Brackets are correct.")
else:
    print("Expression 3: Brackets are not correct.")
