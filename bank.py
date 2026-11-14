from account import SavingAccount, CurrentAccount

class Bank:
    def __init__(self):
        self.accounts= []
        self.next_account_number = 1001

    def create_account(self, name, pin, account_type, balance):
        if len(pin) != 4 or not pin.isdigit():
            print("PIN must be a 4-digit number.")
            return None

        if balance < 500:
            print("Minimum opening balance is Rs. 500")
            return None

        if account_type == '1':
            account = SavingAccount(name, self.next_account_number, pin, balance)

        elif account_type == '2':
            account = CurrentAccount(name, self.next_account_number, pin, balance)

        else:
            print("Invalid account type.")
            return None

        self.accounts.append(account)

        print("\nAccount created successfully")
        print("Account Number :", self.next_account_number)
        self.next_account_number += 1

        return account

    def find_account(self, account_number):
        for i in self.accounts:
            if i.account_number == account_number:
                return i
        return None