###
# A function which returns numbers from 1 to n as a string
#

def numbers(n):
    text = ''
    for i in range(1, n+1):
        text += str(i)
    return text


print(numbers(11))
print(numbers(4))
