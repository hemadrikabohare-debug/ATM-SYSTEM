class BankAccount:
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
        
    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Deposit amount.")
            return False

        self.__balance += amount
        print("Amount deposited successfully.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdrawal amount.")
            return False

        if amount > self.__balance:
            print("Insufficient balance.")
            return False

        self.__balance -= amount
        print("Please collect your cash.")
        return True

    def get_balance(self):
        return self.__balance

    def change_pin(self, old_pin, new_pin):
        if self.__pin != old_pin:
            print("Incorrect old PIN.")
            return False
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("New PIN must be a 4-digit number.")
            return False

        self.__pin = new_pin
        print("PIN changed successfully.")
        return True

    def get_details(self):
        print("\n----- Account Details -----")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print("Balance        :", self.__balance)

# saving account
class SavingAccount(BankAccount):

    def withdraw(self, amount):
        minimum_balance = 500

        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False

        if self.get_balance() - amount < minimum_balance:
            print("Minimum balance of Rs. 500 must be maintained")
            return False
        return super().withdraw(amount)

# current account

class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        return super().withdraw(amount)