###
# A program that calculates how many times the given letter
# appears in any text
#

import letter_counter

text = input('Enter a text: ')
print(f"The number of letter 'e': {letter_counter.counter_of_e(text)}")
