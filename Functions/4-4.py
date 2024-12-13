###
# Calculates the sum of the digits in a number
#


def sum_digits(number):
    total = 0  
    
    abs_number = abs(number)
    
    string_num = str(abs_number)
    
    for i in string_num:
        total += int(i)  # Converting the sign back to a place and adding it to the sum
    
    return total  



any_number = int(input('Number: '))

result = sum_digits(any_number)

print(f'The sum of the digits {any_number} is {result}')
