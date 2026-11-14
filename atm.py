from transaction import Transaction

class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.transaction = {}

    def create_account(self):
        print("\n -----  CREATE ACCOUNT -----")

        name = input("Enter account holder name :")

        print("1. Saving Account")
        print("2. Current Account")
        account_type = input("Select Account type :")

        pin = input("Set 4-digit PIN :")

        try:
            balance = float(input("Enter opening balance: "))
        except ValueError:
            print("Please enter a valid amount")
            return

        account = self.bank.create_account(name, pin, account_type, balance)

        if account is not None:
            self.transaction[account.account_number] = []

    def login(self):
        print("\n ----- ATM LOGIN -----")

        try:
            account_number = int(input("Enter account number :"))
        except ValueError:
            print("Invalid account number!")
            return
        pin = input("Enter 4-digit PIN :")
        account = self.bank.find_account(account_number)

        if account is None:
            print("Account not found")
            return
        if not account.verify_pin(pin):
            print("Incorrect PIN")
            return
        print("\n Login successfull")

        self.account_menu(account)

    def account_menu(self,account):
        while True:
            print("\n ======= ATM MENU =======")
            print("1. Check Balance")
            print("2. Cash Deposit")
            print("3. Cash Withdrawal")
            print("4. Change PIN")
            print("5. Mini Statment")
            print("6. Account Details")
            print("7. Logout")

            choice = input("Enter your choice :")
            if choice == '1':
                print(" Account Balance : Rs.", account.get_balance())
            elif choice == '2':
                try:
                    amount = float(input("Enter  deposit amount :"))
                except ValueError:
                    print("Invalid amount!")
                    continue

                if account.deposit(amount):
                    self.add_transaction(account, "Deposit", amount)

            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount :"))
                except ValueError:
                    print("Invalid amount!")
                    continue
                if account.withdraw(amount):
                    self.add_transaction(account, "Withdrawal", amount)

            elif choice == '4':
                old_pin = input("Enter old PIN :")
                new_pin = input("Enter new 4-digit PIN :")

                account.change_pin(old_pin, new_pin)

            elif choice == '5':
                self.mini_statement(account)

            elif choice == '6':
                account.get_details()

            elif choice == '7':
                print("Logged out successfully")
                break
            else:
                print("Invalid choice! Try again. ")

    def add_transaction(self,account, transaction_type,amount):
        transaction = Transaction(
            transaction_type,
            amount,
            account.get_balance()
        )
        self.transaction[account.account_number].append(transaction)
        
    def mini_statement(self, account):
        print("----- MINI STATEMENT -----")
        history = self.transaction[account.account_number]
        if len(history) == 0:
            print("No transaction available.")
            return

        for i in history:
            i.display()

    def run(self):
        while True:
            print(" ===== Welcome to ATM =====")
            print("1. Create new account")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice :")
            if choice == '1':
                self.create_account()

            elif choice == '2':
                self.login()

            elif choice == '3':
                print("Thank you for using ATM. Goodbye!")
                break
            
            else:
                print("Invalid choice! Try again.")