###
# A program that checks whether if the given string of digits is a valid binary number
#

def binary(binary_number):
    for char in binary_number:
        if char == '0' or char == '1':
            continue
        else:
            return False
    return True


print(binary('101101'))
print(binary('1311a101100'))
