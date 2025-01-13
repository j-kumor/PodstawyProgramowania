import queue

def decimal_to_binary(n):
    # Create a stack
    stack = queue.LifoQueue()
    
    # Repeat division by 2 until the number is zero
    while n > 0:
        remainder = n % 2  # Get the remainder
        stack.put(remainder)  # Push remainder to stack
        n = n // 2  # Divide number by 2
    
    # Pop all elements from the stack and print them
    binary = ""
    while not stack.empty():
        binary += str(stack.get())  # Pop from stack and append to binary string
    
    return binary

# Input natural number
number = 18

# Convert to binary
binary_representation = decimal_to_binary(number)

print("Natural number:", number)
print("Binary number:", binary_representation)
