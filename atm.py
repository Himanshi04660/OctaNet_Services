class ATM:
    # This is the main class representing an ATM, which encapsulates functionalities like balance inquiry, cash withdrawal, deposit, PIN change, and transaction history.
    def __init__(self, initial_balance=0, pin="1234"):
        # The constructor initializes the ATM with an initial balance, a default PIN, and an empty transaction history.
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def authenticate(self):
        # This method authenticates the user by verifying their entered PIN against the stored PIN.
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def balance_inquiry(self):
        # This method displays the current account balance and records the transaction in the history.
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Balance inquiry")

    def cash_withdrawal(self):
        # Handles cash withdrawal by validating the amount and ensuring sufficient balance.
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount > self.balance:
                print("Insufficient funds.")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                self.balance -= amount
                print(f"You have successfully withdrawn ${amount:.2f}.")
                self.transaction_history.append(f"Withdrew ${amount:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def cash_deposit(self):
        # Allows the user to deposit cash into their account, updating the balance and recording the transaction.
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Invalid amount.")
            else:
                self.balance += amount
                print(f"You have successfully deposited ${amount:.2f}.")
                self.transaction_history.append(f"Deposited ${amount:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def change_pin(self):
        # Enables the user to change their PIN after verifying the current PIN and confirming the new PIN.
        old_pin = input("Enter your current PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            confirm_pin = input("Confirm your new PIN: ")
            if new_pin == confirm_pin:
                self.pin = new_pin
                print("PIN changed successfully.")
                self.transaction_history.append("PIN changed")
            else:
                print("New PINs do not match.")
        else:
            print("Incorrect current PIN.")

    def show_transaction_history(self):
        # Displays all recorded transactions, or a message if no transactions have occurred.
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"- {transaction}")

    def main_menu(self):
        # Provides the main user interface, allowing the user to select various ATM functions in a loop.
        while True:
            print("\n--- ATM Menu ---")
            print("1. Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")
            choice = input("Choose an option (1-6): ")

            if choice == "1":
                self.balance_inquiry()
            elif choice == "2":
                self.cash_withdrawal()
            elif choice == "3":
                self.cash_deposit()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # This block initializes the ATM instance, handles authentication, and starts the main menu if authentication is successful.
    atm = ATM(initial_balance=1000)
    if atm.authenticate():
        atm.main_menu()
    else:
        print("Authentication failed. Exiting")