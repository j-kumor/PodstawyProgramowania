# Function to reverse a string using a stack
def reverse_string(input_string):
    # Initialize an empty stack
    stack = []
    
    # Push each character of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Pop characters from the stack to form the reversed string
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Main program to take user input and reverse the string
text = input("Enter text to reverse: ")
reversed_text = reverse_string(text)

print("Reversed text:", reversed_text)
