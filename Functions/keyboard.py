###
# Functions to read any data type from the keyboard
#


def input_string(message):
    string = input(message)
    return string

def input_integer(message):
    number = input(message)
    return int(number)

def input_real(message):
    real_number = input(message)
    return float(real_number)

def input_boolean(message):
    boolean = input(message)
    if boolean == 'y':
        value = True
    else:
        value = False
    return value
