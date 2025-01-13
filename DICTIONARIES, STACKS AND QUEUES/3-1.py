import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# Creates a stack
stack = queue.LifoQueue()

# Put numbers on the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Sum the last two numbers of the stack
# We'll first get the top two elements, sum them, and print the result
last_two_sum = stack.get() + stack.get()  # Get and sum the last two numbers
print("Sum of the last two numbers:", last_two_sum)

# Calculate the sum of the remaining stack elements using a while loop
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print("Sum of the remaining stack elements:", remaining_sum)

"""
Note the order of the printed elements.
The last added element is printed first.
"""