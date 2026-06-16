class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount

account = BankAccount()

account.deposit(500)

print(account.balance)