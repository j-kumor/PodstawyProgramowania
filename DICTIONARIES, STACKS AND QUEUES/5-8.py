# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total_cost = sum(prices[item] * quantity for item, quantity in cart.items())

print(f"Total cost of the shopping cart: ${total_cost:.2f}")
