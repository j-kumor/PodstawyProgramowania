# Ask the user to enter the EAN-13 article number
ean = input("Enter EAN-13 article number: ")

# Check if the entered number has exactly 13 characters and contains only digits
if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    
    # Check if the product is manufactured in Poland (starts with '590')
    if ean.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Invalid article number")