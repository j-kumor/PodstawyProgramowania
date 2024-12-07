# Program to calculate the total amount to pay with discount for more than two products

# Input: number of products purchased and price per product
num_products = int(input("Enter the number of products purchased: "))
product_price = float(input("Enter the price of a product: "))

if num_products > 2:
    total_price = 2 * product_price
    discounted_price = (num_products - 2) * product_price * 0.75
    total_price += discounted_price
else:
    total_price = num_products * product_price

# Output the total amount to pay
print(f"Amount to pay: {total_price:.2f}")