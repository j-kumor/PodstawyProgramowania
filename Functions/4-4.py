###
# Calculates the sum of the digits in a number
#


def sum_digits(number):
    total = 0  # Inicjalizacja sumy na 0
    
    # Pobranie wartości bezwzględnej liczby, aby obsłużyć liczby ujemne
    abs_number = abs(number)
    
    # Konwertowanie liczby bezwzględnej na ciąg znaków, aby przejść po jej cyfrach
    string_num = str(abs_number)
    
    # Iterowanie po każdym znaku (cyfrze) w ciągu znaków reprezentującym liczbę
    for i in string_num:
        total += int(i)  # Konwertowanie znaku z powrotem na liczbę i dodawanie jej do sumy
    
    return total  # Zwracanie całkowitej sumy cyfr


# Pobranie liczby od użytkownika
any_number = int(input('Wprowadź liczbę: '))

# Wywołanie funkcji sum_digits i zapisanie wyniku
result = sum_digits(any_number)

# Wydrukowanie wyniku
print(f'Suma cyfr liczby {any_number} wynosi {result}')