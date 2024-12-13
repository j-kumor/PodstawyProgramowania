###
# A function that returns the n-th value of the Fibonacci sequence.
#

def f(n):
    fibonacci_sequence = [0, 1]  # first two numbers of Fibonacci sequence
    while len(fibonacci_sequence) <= n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence[n-1]


print(f(5))
print(f(9))
