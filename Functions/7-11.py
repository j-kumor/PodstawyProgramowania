###
# A function which returns True if at least one of the number
# n1, n2, n3 is negative or False otherwise
#

def is_neg(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else:
        return False


print(is_neg(11, 6, -4))
print(is_neg(5, 4,  14))
