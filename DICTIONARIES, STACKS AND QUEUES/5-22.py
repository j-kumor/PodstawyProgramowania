import json

# Initialize an empty dictionary to store product data
product = {}

# Read product data from keyboard
product['name'] = input("Enter product name: ")

# Price should be a real number with two decimal places
while True:
    try:
        product['price'] = float(input("Enter product price: "))
        if product['price'] < 0:
            raise ValueError("Price cannot be negative.")
        break
    except ValueError as e:
        print(f"Invalid input for price: {e}. Please enter a valid price.")

# Paid status should be either 'yes' or 'no'
while True:
    paid_input = input("Has the product been paid for (yes/no): ").strip().lower()
    if paid_input == 'yes':
        product['paid'] = True
        break
    elif paid_input == 'no':
        product['paid'] = False
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Save the product data to a JSON file
with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, ensure_ascii=False, indent=4)

print("Product data has been saved to 'product.json'.")
