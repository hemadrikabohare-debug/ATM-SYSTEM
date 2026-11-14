class Transaction:
    def __init__(self,transaction_type, amount, balance):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance

    def display(self):
        print(
            self.transaction_type,
            "| Amount : Rs.",
            self.amount,
            "| Balance : Rs.",
            self.balance
        )