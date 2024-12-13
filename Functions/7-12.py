###
# A function  that returns a string of n asterisks, separated by a slash sign.
#

def asterisks(n):
    text = ''
    for i in range(1, n + 1):
        if i == 1:
            text += '*'
        else:
            text += '/*'
    return text


print(asterisks(4))
print(asterisks(1))