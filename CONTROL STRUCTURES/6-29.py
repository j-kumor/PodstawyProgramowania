def is_prime(num):
    """Sprawdza, czy liczba jest liczbą pierwszą."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # Sprawdzamy dzielniki tylko do pierwiastka z num
        if num % i == 0:
            return False
    return True

def find_primes(n):
    """Zwraca listę pierwszych n liczb pierwszych."""
    primes = []
    num = 2  # Pierwsza liczba pierwsza to 2
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Odczytujemy wartość N od użytkownika
N = int(input("Podaj liczbę N (ilość liczb pierwszych do znalezienia): "))

# Znajdujemy pierwsze N liczb pierwszych
primes = find_primes(N)

# Wyświetlamy liczby pierwsze
print("Liczby pierwsze:", end=" ")
for prime in primes:
    print(prime, end=" ")
