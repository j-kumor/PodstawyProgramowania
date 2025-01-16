# List of products in stock with quantity and unit price
stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

# Calculate the total value using map, lambda, and sum
total_value = sum(map(lambda product: product[0] * product[1], stock))

# Display the result
print(f"Products in stock: {stock}")
print(f"Total value: {total_value:.2f}")
