###
# A function that calculates how many times lettes 'e'
# appears in the text
#

def counter_of_e(text):
    counter = 0
    for i in text:
        if i == 'e' or i == 'E':
            counter += 1
    return counter

if __name__ == "__main__":
    text = 'You never get a second chance to make a first impression'
    print(counter_of_e(text))
