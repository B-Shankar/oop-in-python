# With Encapsulation

class BankAccount:
    def __init__(self):
        self._balance = 0.0 # Protected attribute

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

account = BankAccount()
print(account.balance)
account.deposit(100)
print(account.balance)
account.withdraw(20)
print(account.balance)