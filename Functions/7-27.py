###
# A function that returns True if the product code is correct or False otherwise
# The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7
#

def f(product_code):
    n1 = product_code[0]
    n2 = product_code[1]
    n3 = product_code[2]
    remainder = product_code[3]

    sum_of_three = int(n1) + int(n2) + int(n3)
    if sum_of_three % 7 == int(remainder):
        return True
    else:
        return False


print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
