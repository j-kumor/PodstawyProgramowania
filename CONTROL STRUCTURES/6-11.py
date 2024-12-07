# Program to analyze product price reduction and give a purchase recommendation
current_price = float(input("Enter the current product price: "))
previous_price = float(input("Enter the previous product price: "))

# Calculate the price reduction percentage
price_reduction_percentage = ((previous_price - current_price) / previous_price) * 100

# Check if the price reduction is at least 10%
if price_reduction_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction_percentage:.0f}%")
else:
    print("Price reduction is less than 10%. No recommendation to buy.")