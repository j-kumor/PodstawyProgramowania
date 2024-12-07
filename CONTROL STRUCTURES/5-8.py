# ATM (cash machine) simulator

balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code

def check_pin():
    """Function to check the entered PIN"""
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("PIN verified successfully.")
        return True
    else:
        print("Incorrect PIN. Try again.")
        return False

def change_pin():
    """Function to change the PIN"""
    global pin
    new_pin = input("Enter a new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        pin = new_pin
        print("PIN has been changed successfully.")
    else:
        print("Invalid PIN. The PIN must be exactly 4 digits.")

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        if check_pin():
            print(f"Your current balance is: €{balance}")
    elif choice == '2':
        if check_pin():
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        if check_pin():
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
    elif choice == '4':
        if check_pin():
            print("PIN is correct.")
    elif choice == '5':
        if check_pin():
            change_pin()
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")