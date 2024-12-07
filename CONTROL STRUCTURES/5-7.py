###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

# Function to convert numbers to words for the last five seconds
def number_to_words(number):
    words = ["", "one", "two", "three", "four", "five"]
    if 1 <= number <= 5:
        return words[number]
    return str(number)

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    if countdown <= 5:
        print(number_to_words(countdown))  # Print the last 5 seconds in words
    else:
        print(countdown)  # Print other numbers as usual
    
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")