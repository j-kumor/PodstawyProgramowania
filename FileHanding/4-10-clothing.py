import csv

filename = 'clothing.csv'

products = []

with open(filename, mode='r', newline='') as file:
    # Create a CSV DictReader object
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        products.append(row)

filtered_products = []

for product in products:
    price = float(product['Price'])
    stock = int(product['Stock_Quantity'])
    
    if price < 60 and stock < 40:
        filtered_products.append(product)

for product in filtered_products:
    print(f"{product['Product_Name']}, Price: ${product['Price']}, Stock: {product['Stock_Quantity']}")