# Example

class BankAccount:
    def __init__(self, owner, balance=0):
         self.owner = owner
         self.balance = balance

    def deposit(self, amount):
         self.balance += amount
         print(f"Deposited {amount} into {self.owner}'s account. New balance: {self.balance}")

    def withdraw(self, amount):
         if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account. New balance: {self.balance}")
         else:
            print("Insufficient funds.")

# Create objects
account1 = BankAccount("Sam")
account2 = BankAccount("Saving", 1000)

# Deposit and withdraw
account1.deposit(500)
account2.withdraw(200)