###
# A function that checks whether number is within the range <x, y>
# The function returns a boolean value
#

def num_in_range(number, x, y):
    if x <= number <= y:
        return True
    else:
        return False


if __name__ == "__main__":
    print(num_in_range(2,1,7))
    print(num_in_range(2, 5, 7))