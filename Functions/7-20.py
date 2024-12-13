###
# A function that returns then-th prime number
#


def f(n):
    prime_numbers = []
    number = 2
    #  loop to find prime numbers
    while len(prime_numbers) < n:
        divider = 2
        is_prime = True

        # If we don't find a divisor for half of the number,
        # then number is prime
        while divider * divider <= number:
            if number % divider == 0:
                is_prime = False
                break
            divider += 1  # increase the divider

        #  adding number to table with prime numbers if the number is prime
        if is_prime:
            prime_numbers.append(number)

        number += 1  # increase the number
    return prime_numbers[n-1]


print(f(1))
print(f(5))
