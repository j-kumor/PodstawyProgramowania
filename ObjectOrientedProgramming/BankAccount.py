class BankAccount:
    def __init__(self, account_number):
        """Initializes the bank account with an account number and a balance of PLN 0."""
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: PLN {amount:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account if there are sufficient funds."""
        if amount > self.balance:
            print("Insufficient funds on the account.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawn: PLN {amount:.2f}")
        else:
            print("Withdrawal amount must be greater than zero.")

    def display_account_info(self):
        """Displays the account number and balance."""
        formatted_balance = f"{self.balance:.2f}"
        formatted_account_number = " ".join([self.account_number[i:i+4] for i in range(0, len(self.account_number), 4)])
        print(f"Bank Account No: {formatted_account_number}")
        print(f"Balance: PLN {formatted_balance}")
