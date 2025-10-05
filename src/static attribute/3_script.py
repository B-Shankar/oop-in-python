# Protected and Private Methods

# Protected methods are intended to be used within the class and its subclasses. They are prefixed with a single underscore (_).
# Private methods are intended to be used only within the class itself. They are prefixed with double underscores (__), which triggers name mangling to make it harder to access them from outside the class.

class BankAccount:
    MIN_BALANCE = 100  # Static attribute representing the minimum balance required

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive.")

    # Protected method
    def _valid_amount(self, amount):
        return amount > 0

    # Private method
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ₹{amount}. New balance: ₹{self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5


# Creating an instance of BankAccount
account1 = BankAccount("Alice", 500)
account1.deposit(200)
print("Is 3% a valid interest rate?", BankAccount.is_valid_interest_rate(3))  # True
print("Is 10% a valid interest rate?", BankAccount.is_valid_interest_rate(10))


# Not Recommended
account1._valid_amount(100) # valid, but not recommended
# account1.__log_transaction("withdraw", 50) # invalid, will raise an AttributeError