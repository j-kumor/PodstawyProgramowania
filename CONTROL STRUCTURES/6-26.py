# Correct PIN code
correct_pin = "0805"
# Number of attempts
attempts = 3

# Loop for up to 3 attempts
for i in range(attempts):
    pin = input("Enter the PIN code: ")  # Prompt user to enter PIN
    if pin == correct_pin:
        print("Access granted.")
        break  # Exit the loop if the PIN is correct
    else:
        if i < attempts - 1:  # Only print "Incorrect..." if there are more attempts
            print("Incorrect...")
        else:  # If this is the third attempt, block the card
            print("Sorry, your payment card has been blocked.")
