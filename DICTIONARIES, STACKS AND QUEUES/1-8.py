price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

print("Prices Before Discount:")
total_before_discount = 0
for product, price in price_list.items():
    print(f"{product:<10} ${price:.2f}")
    total_before_discount += price

print(f"\nTotal Value Before Discount: ${total_before_discount:.2f}")

# Apply the 10% discount to each product
discounted_price_list = {product: round(price * 0.90, 2) for product, price in price_list.items()}

print("\nPrices After 10% Discount:")
total_after_discount = 0
for product, price in discounted_price_list.items():
    print(f"{product:<10} ${price:.2f}")
    total_after_discount += price

print(f"\nTotal Value After Discount: ${total_after_discount:.2f}")
