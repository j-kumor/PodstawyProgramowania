from BankAccount import BankAccount

def main():
    # Create a bank account with the specified account number
    account = BankAccount("12345655559090111100007722")

    # Display initial account balance
    account.display_account_info()

    # Deposit PLN 25.30
    account.deposit(25.30)
    account.display_account_info()

    # Try to withdraw PLN 31.70 (insufficient funds)
    account.withdraw(31.70)
    account.display_account_info()

    # Withdraw PLN 14
    account.withdraw(14)
    account.display_account_info()

if __name__ == "__main__":
    main()
