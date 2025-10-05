# Static Methods

# A static method is a method that belongs to the class rather than any specific instance of the class. It does not require access to instance-specific data (i.e., it does not use the self parameter).

# Static methods are defined using the @staticmethod decorator.

# Static Method vs Instance Method:
class BankAccount:
    MIN_BALANCE = 100  # Static attribute representing the minimum balance required

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance after deposit: ₹{self._balance}")
        else:
            print("Deposit amount must be positive.")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


# Creating an instance of BankAccount
account1 = BankAccount("Alice", 500)
account1.deposit(200)
print("Is 3% a valid interest rate?", BankAccount.is_valid_interest_rate(3))  # True
print("Is 10% a valid interest rate?", BankAccount.is_valid_interest_rate(10))

# static methods are used for utility functions that don't need to access instance-specific data.

# They can be called on the class itself without creating an instance.