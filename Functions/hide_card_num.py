###
# A function that masks the card number
#

def hide(card_number):
    hide_number = ''
    for i in range(1, len(card_number) + 1):
        if 2 >= i or i > 12:
            hide_number += card_number[i-1]
        else:
            hide_number += '*'
    return hide_number


if __name__ == "__main__":
    print(hide("5290312400019022"))
