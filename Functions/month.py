###
# Function to print name of the month by its number
#

def month(n):
    # list of month names indexed from 0 to 11
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if 1 <= n <= 12:
        return months[n - 1]  # first index is 0
    else:
        return 'Invalid month number'


if __name__ == "__main__":
    number = 7
    print(f'The name of month {number} is {month(number)}')
