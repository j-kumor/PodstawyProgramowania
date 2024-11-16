
#23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. Then, it calculates and prints both the amount and its VAT. Apply formatting with two decimal places. Sample result:
#Amount  : 15.84
#VAT 23% :  3.64

a = float(input('a='))
vat = a*0.23

print(f'Amount: {a}')
print(f'VAT 23%: {vat:.2f}')
