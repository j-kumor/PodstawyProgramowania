###
# A function that returns True if the expression is a palindrom
#

def f(palindrom):
    for i in range(1, len(palindrom) + 1):
        if palindrom[i-1] == palindrom[-i]:
            continue
        else:
            return False
    return True


print(f('radar'))
print(f('12-11-21'))
print(f('book'))
