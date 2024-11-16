#The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the product price and discount. Print the product price, discount, discounted product price, and the difference between the product price before and after the discount. Print all prices with two decimal places. Sample result:
#Enter price: 24.72
#Enter discount %: 15
#Price with discount: 21.01
#Reduction: 3.71

a = float(input('Enter price: '))
d = float(input('Enter discount %: '))
reduction = (d / 100) * a
discounted_price = a - reduction

print(f'Enter price: {a}')
print(f'Enter discount %: {d}')
print(f'Price with discount: {discounted_price}')
print(f'Reduction: {reduction:.2f}')
