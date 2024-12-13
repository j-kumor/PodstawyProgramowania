###
# A program that calculates the minimum number of coins that
# can be used to pay for the purchased product
#

def coin(amount_to_pay):
    coins = 0
    while amount_to_pay:
        if amount_to_pay >= 5:
            amount_to_pay -= 5
            coins += 1
        elif amount_to_pay >=2:
            amount_to_pay -= 2
            coins += 1
        elif amount_to_pay == 1:
            amount_to_pay -= 1
            coins += 1
    return coins


print(coin(23))
print(coin(8))
print(coin(1))
print(coin(0))
